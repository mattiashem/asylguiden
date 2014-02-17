# Create your models here.
from django.db import models
from mongoengine import *
from mongoengine.django.auth import User

class Post(Document):
    title = StringField(max_length=120, required=True)
    auther = ReferenceField(User) 
    location = ListField(StringField(max_length=40))
    tags = ListField(StringField(max_length=40))
    text = StringField()
