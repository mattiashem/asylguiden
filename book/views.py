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
from mongoengine.queryset import Q
from django import forms
from mongoengine.django.auth import User
from book.models import Post, Question, Media
from users.models import UserInfo
from django.views.decorators.http import require_POST
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
import hashlib
from django.core.mail import send_mail, BadHeaderError


from mongoengine import *
from django.contrib import auth

class User(User):
    location =  GeoPointField()

def start(request):
    return render_to_response('book/index.html',context_instance=RequestContext(request))

@login_required
def new(request):
	c = {}
	c.update(csrf(request))
	
	if request.method == 'POST':
		currentuser = User.objects.get(id=request.user.id)
		
		#Tags	
		incommingtags=request.POST["tags"].replace(" ","")
		thetags=incommingtags.split(',')

		#Location
		incommingloca=request.POST["location"].replace(" ","")
		thelocations=incommingloca.split(',')

		#Saving articel
		articel=Post(title=request.POST['title'],auther=currentuser,location=thelocations,tags=thetags,text=request.POST["text"])
		articel.save()	 
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


def question(request):
	'''
	Show articels in databas
	'''
	articels = Question.objects()
	return render_to_response('book/qarticels.html',  {'articels': articels},context_instance=RequestContext(request))


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
		Articels = Question.objects(Q(tags=search) | Q(where=search))
		print Articels
		return render_to_response('book/qsearch.html', {'articels': Articels},context_instance=RequestContext(request))

	else:
		return render_to_response('book/qsearch.html',context_instance=RequestContext(request) )



def articels(request):
	'''
	Show articels in databas
	'''
	articels = Post.objects()
	return render_to_response('book/articels.html',  {'articels': articels},context_instance=RequestContext(request))

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
		Articels = Post.objects(Q(tags=search) | Q(location=search))
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
	
	articels = Post.objects(id=id)
	return render_to_response('book/articels.html',  {'articels': articels},context_instance=RequestContext(request))

def view_tags(request,tags):
	'''
	View and articel
	'''
	
	articels = Post.objects(tags=tags)
	return render_to_response('book/list_articels.html',  {'articels': articels},context_instance=RequestContext(request))

def view_location(request,locations):
	'''
	View and articel
	'''
	
	articels = Post.objects(location=locations)
	return render_to_response('book/list_articels.html',  {'articels': articels},context_instance=RequestContext(request))
	

@login_required
def view_delete(request,id):
	'''
	view and articel
	'''
	currentuser = User.objects.get(id=request.user.id)
	info ="no"
	
	if request.method == 'POST':
		articel = Post(id=id,auther=currentuser)
		articel.delete()
		info ="delete"

	articels = Post.objects(id=id,auther=currentuser)
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

		articel.title=request.POST.get('title')
		articel.location=thelocations
		articel.tags=thetags
		articel.text=request.POST.get('text')
		articel.save()
		info ="update"


	
	articels = Post.objects(id=id,auther=currentuser)
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
    return render_to_response('book/media.html',{'media':os.listdir(settings.STATIC_ROOT+"/user/"+str(hashlib.sha224(str(request.user.id)).hexdigest())), 'dest':settings.STATIC_URL+"/user/"+str(hashlib.sha224(str(request.user.id)).hexdigest())+"/"}, context_instance=RequestContext(request))

@login_required
def upload_file(request):
    info="no"
    if request.method == 'POST':
        print "is post"
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'],request.FILES['file'].name, hashlib.sha224(str(request.user.id)).hexdigest())
            info="Uploaded"
    else:
        form = UploadFileForm()
    return render_to_response('book/myupload.html', {'form': form, 'info':info}, context_instance=RequestContext(request))



def handle_uploaded_file(f,name,id):

    if not os.path.isdir(settings.STATIC_ROOT+"/user/"+str(id)):
        os.mkdir(settings.STATIC_ROOT+"/user/"+str(id))
    with open(settings.STATIC_ROOT+"/user/"+str(id)+"/"+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)