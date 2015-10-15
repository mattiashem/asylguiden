# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from djangotoolbox.fields import ListField


<<<<<<< HEAD
class Post(models.Model):
    title = models.CharField(max_length=120)
    auther = models.CharField(max_length=120)
    location = ListField()
    tags = ListField()
    page_views = models.FloatField()
    page_rate = models.FloatField()
    text = models.TextField()
=======
class Post(Document):
    title = StringField(max_length=120, required=True)
    auther = ReferenceField(User) 
    location = ListField(StringField(max_length=40))
    tags = ListField(StringField(max_length=40))
    page_views = IntField()
    page_rate = IntField()
    text = StringField()
>>>>>>> d4e9b9a8f34944a3e045ff50c81afcfb9e32377c


class Question(models.Model):
    title = models.CharField(max_length=120)
    auther = models.CharField(max_length=120)
    where = ListField()
    tags = ListField()
    text = models.TextField()

#class Media(models.Model):
#    file = models.FileField(storage=gridfs_storage, upload_to='/')
