from django import template
from django.template import Library, Node
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

from mongoengine import *
from django.contrib import auth
register = template.Library()

class User(User):
    location =  GeoPointField()

class UserInfoNode(Node):

	def render(self, context):
		userinfo = UserInfo.objects.filter(id='50c0a4dded8f5b082c235570')
		context['userinfo'] = userinfo
		return ''
		
@register.tag(name='get_user_info')
def get_user_info(parser, token):
	return UserInfoNode()



#Gett top 10 locations


class GetTopLocation(Node):

	def render(self, context):
		locations_freqs = Post.objects.item_frequencies('location', normalize=True)
		esorted = sorted(locations_freqs.items(), key=itemgetter(1), reverse=True)[:10]
		return_list=[]
		for i in esorted:
			return_list.append(i[0])

		context['top_locations'] = return_list
		return ''
		
@register.tag(name='get_top_location')
def get_top_location(parser, token):
	return GetTopLocation()





#Get all locations
class GetLocation(Node):

	def render(self, context):
		locations_freqs = Post.objects.item_frequencies('location', normalize=True)
		esorted = sorted(locations_freqs.items(), key=itemgetter(1), reverse=True)
		return_list=[]
		for i in esorted:
			return_list.append(i[0])

		context['locations'] = return_list

		return ''
		
@register.tag(name='get_location')
def get_location(parser, token):
	return GetLocation()


#Get Tags

class GetTopTags(Node):

	def render(self, context):
		tags_freqs = Post.objects.item_frequencies('tags', normalize=True)
		esorted = sorted(tags_freqs.items(), key=itemgetter(1), reverse=True)[:10]
		return_list=[]
		for i in esorted:
			return_list.append(i[0])

		context['top_tags'] = return_list
		return ''
		
@register.tag(name='get_top_tags')
def get_top_tags(parser, token):
	return GetTopTags()




#Get all tags
class GetTags(Node):

	def render(self, context):
		tags_freqs = Post.objects.item_frequencies('tags', normalize=True)
		esorted = sorted(tags_freqs.items(), key=itemgetter(1), reverse=True)
		return_list=[]
		for i in esorted:
			return_list.append(i[0])

		context['tags'] = return_list
		return ''
		
@register.tag(name='get_tags')
def get_tags(parser, token):
	return GetTags()




class ArticelNode(Node):

	def render(self, context):
		#currentuser = User.objects.get(id=request.user.id)
		#users_articel = Post.objects(auther=currentuser)
		#context['users_articel'] = users_articel 
		return ''
		
@register.tag(name='get_users_articel')
def get_users_articel(parser, token):
	return ArticelNode()