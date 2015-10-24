# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,  login
from book.models import Post
from users.models import UserInfo
import datetime
import hashlib
from email_control import welcome_email
from django.shortcuts import redirect







def register(request):
	'''
	Register an new user
	'''
	c = {}
	c.update(csrf(request))
	info = "no"
	if request.method == 'POST':
			user = User.objects.filter(username=request.POST['email'])
			print user
			if user:
				info= "error"
				return render_to_response("users/register.html", {'info': info}, context_instance=RequestContext(request))
			else:
				User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password1'])
				user = authenticate(username=request.POST['email'], password=request.POST['password1'])
				print user
				if user is not None:
					if user.is_active:
						login(request, user)
						print "logged in"
						User_info = UserInfo.objects.get_or_create(user=user, username=request.POST['email'],postscount=0,read=0)
						if welcome_email(request.POST['email'],request.POST['email']):
							print "Welcome email sent"
						#signup_mailchump(request.POST['email'])
						return HttpResponseRedirect("/users/mypage")
			return HttpResponseRedirect("/users/register")

			info = "error"
			return render_to_response("users/register.html", {'info': info}, context_instance=RequestContext(request))
	else:
		return render_to_response("users/register.html", {'info': info}, context_instance=RequestContext(request))


def web_login(request):
	'''
	loggin the user
	'''
	c = {}
	c.update(csrf(request))
	info = "no"
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		print user
		if user is not None:
			# the password verified for the user
			if user.is_active:
				login(request,user)
				print("User is valid, active and authenticated")
				#User_info = UserInfo.objects.get_or_create(user=user, username=request.POST['username'],postscount=0,read=0)
				return HttpResponseRedirect("/users/mypage")
			else:
				print("The password is valid, but the account has been disabled!")
		else:
			#the authentication system was unable to verify the username and password
			print("The username and password were incorrect.")

	return render_to_response("users/login.html", {'info': info}, context_instance=RequestContext(request))




def resetpassword(request,keys):
	'''
	Verifying the key and then resetting the password.
	'''
	userInfo = UserInfo.objects.get(reset_password_key=keys)
	#user = User.objects.get.(username=userInfo.username)
	print user

	return render_to_response("users/resett_password.html",c,context_instance=RequestContext(request))



def lostpassword(request):
	'''
	Logging the user out
	'''
	info ="no"
	if request.method == 'POST':
		'Resetting Password'
		print "resetting password"
		submit_email = request.POST.get('email')
		print submit_email
		try:
			theuser = User.objects.get(email=submit_email)
			theuser_info = UserInfo.objects.get(user=theuser)
			#making hash for user redir
			length = 50
			chars = string.ascii_letters + string.digits + '!@#$%^&*()'
			random.seed = (os.urandom(1024))
			theuser_info.reset_password_key = ''.join(random.choice(chars) for i in range(length))
			theuser_info.reset_password_date = datetime.datetime.now()
			theuser_info.save()
			#Sending email to user
		#send_mail('Password Resetting at Asylguiden', 'This is you password resetting from asylguiden \n Press this link to resett ypu password', 'system@asylguiden.se',
		#		[theuser.email], fail_silently=False)
			info = "reset"

		except:
			info = "error"



		return render_to_response("users/lost_password.html",{'info':info},context_instance=RequestContext(request))


	c = {}
	c.update(csrf(request))
	auth.logout(request)
	return render_to_response("users/lost_password.html",{'info':info},context_instance=RequestContext(request))		


def user(request,username):
	'''
	Show the user profile OPEN
	'''


	print username
	user = UserInfo.objects.get(username=username)
	user_2 = User.objects.get(username=username)
	return render_to_response("users/user.html",{'user_id':user_2.id,'userinfo':user},context_instance=RequestContext(request))



def logout(request):
	'''
	Logging the user out
	'''
	auth.logout(request)
	return HttpResponseRedirect("/book/start")

def mypage(request):
	'''
	Show the users my page
	'''
	if request.user.is_authenticated():
		#No info
		info="no"
		#Updating user settingsglobal name 'request' is not defined
		if request.POST.get("user_settings"):
			user = User.objects.get(id=request.user.id)
			if request.POST.get('password1'):
				user.set_password(request.POST.get('password1'))
			if request.POST.get('email'):
				user.email = request.POST.get('email')
			user.save()
			info = "saved"
		#updating user details in mongodb
		if request.POST.get("user_detial"):
			user = User.objects.get(id=request.user.id)
			update = UserInfo.objects.get(user=user)
			update.username = request.user.username
			update.first_name = request.POST.get('id_fname')
			update.last_name = request.POST.get('id_sname')
			update.address = request.POST.get('id_address')
			update.postnr = request.POST.get('id_postnr')
			update.cell = request.POST.get('id_cell')
			update.country = request.POST.get('id_country')
			update.language = request.POST.get('id_language')
			update.save()
			info = "saved"

		#Get user info fix for displying correct user email after update
		user_info = User.objects.get(id=request.user.id)
		userid   = request.user.id
		print user_info
		username = request.user.username
		useremail = user_info.email


		currentuser = UserInfo.objects.get(user=user_info)
		print currentuser
		try:
			users_articel = Post.objects.filter(auther=username)
		except:
			users_articel =[]


		return render_to_response("users/mypage.html",{'user_id':str(hashlib.sha224(str(request.user.id)).hexdigest()),'username':username,'useremail':useremail,'userid':userid,'users_articel':users_articel,'info':info,'userinfo':currentuser},context_instance=RequestContext(request))

	else:
		 return redirect('/')



def signup_mailchump(email):
	'''
	Sign upp new user to our mailchimp email service
	All new usere that sign up will get sign up to automatical
	'''
	chimp = chimpy.Connection('d784f29c89de4f56fc793d85a074623c-us8')
	chimp.list_subscribe('be2d53aa4d', email, {'FIRST': 'User', 'LAST': 'Asylguiden'}, double_optin=False)
	#No info
	info="no"
	#Updating user settingsglobal name 'request' is not defined
	if request.POST.get("user_settings"):
		user = User.objects.get(id=request.user.id)
		if request.POST.get('password1'):
			user.set_password(request.POST.get('password1'))
		if request.POST.get('email'):
			user.email = request.POST.get('email')
		user.save()
		info = "saved"
	#updating user details in mongodb	
	if request.POST.get("user_detial"):
		user = User.objects.get(id=request.user.id)
		update = UserInfo.objects.get(user=user)
		update.username = request.user.username
		update.first_name = request.POST.get('id_fname')
		update.last_name = request.POST.get('id_sname')
		update.address = request.POST.get('id_address')
		update.postnr = request.POST.get('id_postnr')
		update.cell = request.POST.get('id_cell')
		update.country = request.POST.get('id_country')
		update.language = request.POST.get('id_language')
		update.save()
		info = "saved"

	#Get user info fix for displying correct user email after update
	user_info = User.objects.get(id=request.user.id)
	userid   = request.user.id
	username = request.user.username
	useremail = user_info.email


	currentuser = UserInfo.objects(user=user_info)
	users_articel = Post.objects(auther=user_info)



	return render_to_response("users/mypage.html",{'user_id':str(hashlib.sha224(str(request.user.id)).hexdigest()),'username':username,'useremail':useremail,'userid':userid,'users_articel':users_articel,'info':info,'userinfo':currentuser},context_instance=RequestContext(request))

def signup_mailchump(email):
    '''
    Sign upp new user to our mailchimp email service
    All new usere that sign up will get sign up to automatical
    '''
    chimp = chimpy.Connection('d784f29c89de4f56fc793d85a074623c-us8')
    chimp.list_subscribe('be2d53aa4d', email, {'FIRST': 'User', 'LAST': 'Asylguiden'}, double_optin=False)
