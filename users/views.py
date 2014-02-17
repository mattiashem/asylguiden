# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Library
from django.http import HttpResponseRedirect
from operator import itemgetter
from mongoengine.queryset import Q
from django import forms
from mongoengine.django.auth import User
from book.models import Post
from users.models import UserInfo
from django.core.mail import send_mail
from django.conf import settings
import os, random, string
from mongoengine import *
from django.contrib import auth
import datetime




class User(User):
    location =  GeoPointField()


def register(request):
	'''
	Register an new user
	'''
	c = {}
	c.update(csrf(request))
	info="no"
	if request.method == 'POST':
		try:
			User.create_user(request.POST['username'],request.POST['password1'],request.POST['email'])
			user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
			if user is not None and user.is_active:
				auth.login(request,user)
				User_info=UserInfo.objects.get_or_create(user=user,username=request.POST['username'])
				return HttpResponseRedirect("/users/mypage")

		except:
			info = "error"
			return render_to_response("users/register.html",{'info':info},context_instance=RequestContext(request))
	else:
		return render_to_response("users/register.html",{'info':info},context_instance=RequestContext(request))



def login(request):
	'''
	loggin the user
	'''
	c = {}
	c.update(csrf(request))
	info="no"
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username,password=password)
		if user is not None and user.is_active:
			auth.login(request,user)
			User_info=UserInfo.objects.get_or_create(user=user,username=request.POST['username'])
			return HttpResponseRedirect("/users/mypage")
		else:
			info="error"
	
	return render_to_response("users/login.html",{'info':info},context_instance=RequestContext(request))		

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


	
	return render_to_response("users/mypage.html",{'username':username,'useremail':useremail,'userid':userid,'users_articel':users_articel,'info':info,'userinfo':currentuser},context_instance=RequestContext(request))

