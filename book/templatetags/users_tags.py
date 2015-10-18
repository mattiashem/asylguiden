from django import template
from django.template import Library, Node
# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Library
from django.http import HttpResponseRedirect
from operator import itemgetter
from django import forms
from django.contrib.auth.models import User
from book.models import Post
from users.models import UserInfo
from django.db.models import Count

from django.contrib import auth
register = template.Library()

#class User(User):
#    location =  GeoPointField()

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
		locations_freqs = Post.objects.all()
		get_top_loc=[]

		for loc in locations_freqs:
			for l in loc.location:
				print l
				get_top_loc.append(l)
		context['top_locations'] = get_top_loc
		return ''
		
@register.tag(name='get_top_loc')
def get_top_location(parser, token):
	return GetTopLocation()





#Get all locations
class GetLocation(Node):

	def render(self, context):
		locations = Post.objects.order_by('location')
		context['locations'] = locations

		return ''
		
@register.tag(name='get_location')
def get_location(parser, token):
	return GetLocation()


#Get Tags

class GetTopTags(Node):

	def render(self, context):
		tags_freqs = Post.objects.all()
		get_top_freqs=[]

		for tag in tags_freqs:
			for t in tag.tags:
				get_top_freqs.append(t)

		context['top_tags'] = get_top_freqs
		return ''
		
@register.tag(name='get_top_tags')
def get_top_tags(parser, token):
	return GetTopTags()




#Get all tags
class GetTags(Node):

	def render(self, context):
		tags = Post.objects.order_by('tags')
		context['tags'] = tags
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