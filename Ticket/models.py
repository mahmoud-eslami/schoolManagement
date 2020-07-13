from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.conf import settings


class Ticket (models.Model):
    id = models.AutoField(primary_key = True)
    senderId =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='sender')
    resiverId = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name = 'resiver')
    content = models.CharField(max_length=5000,blank=False,null=True)
    title = models.CharField(max_length=255,blank=False,null=True,unique=True)
    is_colse = models.CharField(max_lengh=1,blank=False, null =False ,default = 'False' )
    is_awnserd = models.CharField(max_lengh =1, blank = False,null = True,defaul = 'False')

    #releaseTime = models.CharField(max_lenght =3 ,blank = False , null = False ) 
    #date
    
