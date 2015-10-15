# Create your models here.
from django.db import models
from djangotoolbox.fields import ListField

<<<<<<< HEAD
class UserInfo(models.Model):
    user = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=50,null=True)
    postnr = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50,null=True)
    language = models.CharField(max_length=50,null=True)
    cell = models.CharField(max_length=50,null=True)
    #reset_password_key = models.CharField(max_length=50)
    #reset_password_date = models.DateTimeField()
    postscount = models.FloatField(max_length=50)
    read = models.FloatField(max_length=50)
=======
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
    postscount = IntField()
    read = IntField()
>>>>>>> d4e9b9a8f34944a3e045ff50c81afcfb9e32377c



