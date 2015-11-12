# Create your views here.
import os
from django.core.context_processors import csrf
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Library
from django.http import HttpResponseRedirect ,HttpResponse
from operator import itemgetter
from django.db.models import Q
from django import forms
from django.contrib.auth.models import User
from book.models import Post, Question
from users.models import UserInfo
from django.views.decorators.http import require_POST
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
import hashlib
from django.core.mail import send_mail, BadHeaderError
from django.db.models import F
from itertools import chain
from django.shortcuts import redirect
from share.twitter_connect import send_to_twitter
from share.facebook_connect import post_to_facebook
from PIL import Image
import PIL.ImageOps



def start(request):
    return render_to_response('book/index.html',context_instance=RequestContext(request))


def get_user_settings(id):

        if id == None:
            print "get all laguages"
            return True
        else:
            print id
            currentuser = User.objects.get(id=id)
            lan = UserInfo.objects.get(username=currentuser)
            print lan.country
            print lan.language
            dict = {'country': lan.country, 'language': lan.language};
            return dict


@login_required
def new(request):
    c = {}
    c.update(csrf(request))

    if request.method == 'POST':
        currentuser = User.objects.get(id=request.user.id)
        print currentuser


        #Tags
        incommingtags=request.POST["tags"].replace(" ","")
        thetags=incommingtags.split(',')


        #Location
        incommingloca=request.POST["location"].replace(" ","")
        thelocations=incommingloca.split(',')

        #Saving articel
        articel=Post(title=request.POST['title'],auther=currentuser,location=thelocations,tags=thetags,text=request.POST["text"],page_views=0,page_rate=0,language=request.POST["language"],country=request.POST["country"])
        articel.save()
        UserInfo.objects.select_related().filter(username=currentuser).update(postscount=F('postscount')+1)
        #Sharing
        try:
            send_to_twitter(request.POST['title'],str(thetags[0]),str(thelocations[0]))
            post_to_facebook(request.POST['title'],str(thetags[0]),str(thelocations[0]))
        except :
            print "Error sharing posts"
        return render_to_response('book/saved.html',context_instance=RequestContext(request))


    return render_to_response('book/new.html', c,context_instance=RequestContext(request))


@login_required
def writeqestion(request):
	c = {}
	c.update(csrf(request))

	if request.method == 'POST':
		currentuser = User.objects.get(id=request.user.id)

		#Tags
		incommingtags=request.POST["tags"].replace(" ","")
		thetags=incommingtags.split(',')

		#Location
		where=request.POST["where"].replace(" ","")
		thewhere=where.split(',')

		#Saving articel
		quest=Question(title=request.POST['quest'],auther=currentuser,where=thewhere,tags=thetags,text=request.POST["text"])
		quest.save()
		return render_to_response('book/saved.html',context_instance=RequestContext(request))


	return render_to_response('book/qestion.html', c,context_instance=RequestContext(request))

@login_required
def rate(request):
    '''
    Rate the articel
    '''
    if request.method == 'POST':
        if request.user.id:
            currentuser = User.objects.get(id=request.user.id)

            Post.objects(id=request.POST.get('articel')).update_one(inc__page_rate=int(request.POST.get('rate')))
            return render_to_response('book/rate_ok.html',context_instance=RequestContext(request))
        else:
            print "User not login"
            return render_to_response('book/rate_no.html',context_instance=RequestContext(request))
    return render_to_response('book/rate_no.html',context_instance=RequestContext(request))

def question(request):
    '''
    Show articels in databas
    '''
    try:
        articels = Question.objects.all()
    except:
        articels=[]
    return render_to_response('book/list_questions.html',  {'articels': articels},context_instance=RequestContext(request))


def searchquestion(request):
	'''
	Searching trow articels for match.
	Search in both tags, Locations and articel text
	'''
	#Ceating CSRF
	c = {}
	c.update(csrf(request))

	if request.method == 'POST':
		search=request.POST['search']
		Articels = Question.objects(Q(tags=search) | Q(where=search) | Q(language=request.POST["language"]))
		print Articels
		return render_to_response('book/qsearch.html', {'articels': Articels},context_instance=RequestContext(request))

	else:
		return render_to_response('book/qsearch.html',context_instance=RequestContext(request) )



def articels(request):
    '''
    Show articels in databas
    '''
    u_dict = get_user_settings(request.user.id)
    if u_dict:
        articels = Post.objects.all()
    else:
        articels = Post.objects.filter(language=u_dict['language'], country=u_dict['country'])
    return render_to_response('book/list_articels.html',  {'articels': articels},context_instance=RequestContext(request))

def top_ten_tags(request):
	'''
	Getting the top ten tags
	'''
	tag_freqs = Post.objects.item_frequencies('tags', normalize=True)
	top_tags = sorted(tag_freqs.items(), key=itemgetter(1), reverse=True)[:10]
	return render_to_response('book/tags.html',  {'tags': top_tags},context_instance=RequestContext(request))	

def top_ten_location(request):
	'''
	Getting the top ten locations
	'''
	locations_freqs = Post.objects.item_frequencies('location', normalize=True)
	top_location = sorted(locations_freqs.items(), key=itemgetter(1), reverse=True)[:10]
	return render_to_response('book/locations.html',  {'location': top_location},context_instance=RequestContext(request))


def search_articels(request):
    '''
    Searching trow articels for match.
    Search in both tags, Locations and articel text
    '''
    #Ceating CSRF
    c = {}
    c.update(csrf(request))

    if request.method == 'POST':
        search=request.POST['search']
        Articels_1 = Post.objects.filter(Q(tags=search) | Q(location=search))
        Articels_2 = Post.objects.filter(Q(title=search))
        Articels = list(chain(Articels_1, Articels_2))

        print Articels
        return render_to_response('book/search.html', {'articels': Articels},context_instance=RequestContext(request))

    else:
        return render_to_response('book/search.html',context_instance=RequestContext(request) )

def view_location_tags(request,location,tags):
	'''
	View and articel
	'''
	
	articels = Post.objects(Q(tags=tags) | Q(location=location))
	return render_to_response('book/list_articels.html',  {'articels': articels},context_instance=RequestContext(request))





def view_articel(request,id):
    '''
    View and articel
    '''
    Post.objects.select_related().filter(id=id).update(page_views=F('page_views')+1)
    articels = Post.objects.get(id=id)
    a = articels
    UserInfo.objects.select_related().filter(username=a.auther).update(read=F('read')+1)
    theuser = UserInfo.objects.get(username=a.auther)
    print theuser

    return render_to_response('book/articels.html',  {'articels': articels, 'auther': theuser },context_instance=RequestContext(request))


def view_question(request,id):
    '''
    View and articel
    '''
    #Post.objects.select_related().filter(id=id).update(page_views=F('page_views')+1)
    articels =Question.objects.get(id=id)
    a = articels
    UserInfo.objects.select_related().filter(username=a.auther).update(read=F('read')+1)
    theuser = UserInfo.objects.get(username=a.auther)


    return render_to_response('book/qarticels.html',  {'articels': articels, 'auther': theuser },context_instance=RequestContext(request))


def view_tags(request,tags):
	'''
	View and articel
	'''
	
	articels = Post.objects.filter(tags=tags)
	return render_to_response('book/list_articels.html',  {'articels': articels},context_instance=RequestContext(request))

def view_location(request,locations):
	'''
	View and articel
	'''
	
	articels = Post.objects.filter(location=locations)
	return render_to_response('book/list_articels.html',  {'articels': articels},context_instance=RequestContext(request))


@login_required
def view_delete(request,id):
    '''
    view and articel
    '''
    currentuser = User.objects.get(id=request.user.id)
    info ="no"

    if request.method == 'POST':
        articel = Post.objects.get(id=id,auther=currentuser)
        articel.delete()
        info ="delete"
        return redirect('/users/mypage')

    articels = Post.objects.get(id=id,auther=currentuser)
    return render_to_response('book/delete_articels.html',  {'articels': articels,'info':info},context_instance=RequestContext(request))

@login_required
def view_change(request,id):
    '''
    view and articel
    '''
    currentuser = User.objects.get(id=request.user.id)

    #displaying no info
    info ="no"


    if request.method == 'POST':
        articel = Post(id=id,auther=currentuser)
        #Tags
        incommingtags=request.POST["tags"].replace(" ","")
        thetags=incommingtags.split(',')

        #Location
        incommingloca=request.POST["location"].replace(" ","")
        thelocations=incommingloca.split(',')
        Post.objects.filter(id=id,auther=currentuser).update(title=request.POST.get('title'),location=thelocations,tags=thetags,text=request.POST.get('text'))

        info ="update"



    articels = Post.objects.get(id=id,auther=currentuser)
    return render_to_response('book/change_articels.html',  {'articels': articels,'info':info},context_instance=RequestContext(request))

def about(request):
    info = "no"
    if request.method == 'POST':
        #Ceating CSRF
        c = {}
        c.update(csrf(request))
        info ="saved"
        subject = request.POST['subject']
        message = request.POST['text']
        from_email = request.POST['from_email']
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['mattias@asylguiden.se'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render_to_response('book/about.html',{'info':info},context_instance=RequestContext(request))

def support(request):
    return render_to_response('book/support.html',context_instance=RequestContext(request))

def supporters(request):
    return render_to_response('book/supporters.html',context_instance=RequestContext(request))

def help(request):
    return render_to_response('book/help.html',context_instance=RequestContext(request))

def tech(request):
    return render_to_response('book/tech.html',context_instance=RequestContext(request))

@login_required
def media(request):
    #Getting the media for the user

    images = [".jpg", ".png", ".gif", ".JPG", ".PNG", ".GIF"]
    movies = [".mp4", ".MP4"]
    media=[]
    if request.GET['type'] == "image":
    #Show images to user
        for file in os.listdir(settings.STATIC_ROOT+"/user/"+str(hashlib.sha224(str(request.user.id)).hexdigest())):
            if file.endswith(tuple(images)):
                media.append(file)

    if request.GET['type'] == "media":
    #Show movies to user
        for file in os.listdir(settings.STATIC_ROOT+"/user/"+str(hashlib.sha224(str(request.user.id)).hexdigest())):
            if file.endswith(tuple(movies)):
                media.append(file)

    #Send data back to user
    return render_to_response('book/media.html',{'media':media, 'dest':settings.STATIC_URL+"/user/"+str(hashlib.sha224(str(request.user.id)).hexdigest())+"/",'thumb':settings.STATIC_URL+"/thumb/"+str(hashlib.sha224(str(request.user.id)).hexdigest())+"/"}, context_instance=RequestContext(request))

@login_required
def upload_file(request):
    info="no"
    print "user " + str(request.user.id)
    #Approved file extenasions
    images = [".jpg", ".png", ".gif", ".JPG", ".PNG", ".GIF"]
    movies = [".mp4", ".MP4"]
    if request.method == 'POST':
        # WHEN AN IMAGES IS UPLOADED
        if request.FILES['file'].name.endswith(tuple(images)):
            if request.method == 'POST':
                form = UploadFileForm(request.POST, request.FILES)
                if form.is_valid():
                    #If the form is good process the file for update

                    handle_uploaded_file(request.FILES['file'],request.FILES['file'].name, request.user.id)
                    if "profile" == request.POST['profile']:
                        #If profile images is used send file to be the profile images
                        profile_file(request.FILES['file'],request.FILES['file'].name, request.user.id)
                    info="Uploaded"
        #WHEN AN MOVIE IS UPLOADED
        elif request.FILES['file'].name.endswith(tuple(movies)):
                if request.method == 'POST':
                    form = UploadFileForm(request.POST, request.FILES)
                    if form.is_valid():
                        #If the form is good process the file for update
                        handle_uploaded_movie(request.FILES['file'],request.FILES['file'].name.replace(' ','_'), hashlib.sha224(str(request.user.id)).hexdigest())
                    info="Uploaded"
        else:
            info="ERROR_FILETYPE"
            form = UploadFileForm()
    else:
        form = UploadFileForm()
    return render_to_response('book/myupload.html', {'form': form, 'info':info}, context_instance=RequestContext(request))

def profile_file(f,name,id):
    '''
    Making the profile photo for users
    '''
    with open("/code/static/profile/"+str(id)+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    image = Image.open("/code/static/profile/"+str(id)+name)
    # ImageOps compatible mode
    if image.mode not in ("L", "RGB"):
        image = image.convert("RGB")

    image.thumbnail((200,200), Image.ANTIALIAS)
    image.save("/code/static/profile/thumb_"+str(id)+".jpg", 'JPEG', quality=75)

def handle_uploaded_movie(f,name,id):
    '''
    Uploading the movie to the correct folder
    And transcode the movie if its not mp4 format and used for html5 standards
    '''
    if not os.path.isdir("/code/static/user/"+str(id)):
        os.mkdir("/code/static/user/"+str(id))
    with open("/code/static/user/"+str(id)+"/"+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_file(f,name,id):
    '''
    Uploading and rezecing imgaes uploaded from userscd ..
    '''

    if not os.path.isdir("/code/static/user/"+str(id)):
        os.mkdir("/code/static/user/"+str(id))
    with open("/code/static/user/"+str(id)+"/"+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    image = Image.open("/code/static/user/"+str(id)+"/"+name)

    #Making thumbnail and images in differnt sizes
    if not os.path.isdir("/code/static/thumb/"+str(id)):
        os.mkdir("/code/static/thumb/"+str(id))

    # ImageOps compatible mode
    if image.mode not in ("L", "RGB"):
        image = image.convert("RGB")

    #fname=name.split('.')

    imageresize = image.resize((200,200), Image.ANTIALIAS)
    imageresize.save("/code/static/thumb/"+str(id)+"/resize_200_200"+name+".jpg", 'JPEG', quality=75)

    image.thumbnail((200,200), Image.ANTIALIAS)
    image.save("/code/static/thumb/"+str(id)+"/thumpnail_"+name+".jpg", 'JPEG', quality=75)

    imagefit = PIL.ImageOps.fit(image, (200, 200), Image.ANTIALIAS)
    imagefit.save("/code/static/thumb/"+str(id)+"/fit_"+name+".jpg", 'JPEG', quality=75)