from django.db import models
from django.db.models. fields import CharField, IntegerField, BooleanField, TextField, DateTimeField

class User(models.Model):

    email = models.CharField(max_length=40)
    username = models.CharField(max_length=10)
    password = models.TextField()
    is_admin = models.BolleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    followers = models.IntegerField()
    followings = models.IntegerField()

    
# Create your models here.
