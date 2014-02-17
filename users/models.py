# Create your models here.
from django.db import models
from mongoengine import *
from mongoengine.django.auth import User

class UserInfo(Document):
	user = ReferenceField(User) 
	username = StringField(required=True)
	first_name = StringField(max_length=50)
	last_name = StringField(max_length=50)
	address = StringField(max_length=50)
	postnr = StringField(max_length=50)
	country = StringField(max_length=50)
	language = StringField(max_length=50)
	cell = StringField(max_length=50)
	reset_password_key = StringField(max_length=50)
	reset_password_date = DateTimeField()



