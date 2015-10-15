# Create your models here.
from django.db import models
from djangotoolbox.fields import ListField

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



