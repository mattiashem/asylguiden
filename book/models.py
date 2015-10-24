# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from djangotoolbox.fields import ListField



class Post(models.Model):
    title = models.CharField(max_length=120)
    auther = models.CharField(max_length=120)
    language = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    location = ListField()
    tags = ListField()
    page_views = models.FloatField()
    page_rate = models.FloatField()
    text = models.TextField()



class Question(models.Model):
    title = models.CharField(max_length=120)
    auther = models.CharField(max_length=120)
    where = ListField()
    tags = ListField()
    text = models.TextField()

#class Media(models.Model):
#    file = models.FileField(storage=gridfs_storage, upload_to='/')
