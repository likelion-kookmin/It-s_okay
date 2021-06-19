from django.db import models
from django.contrib.auth.models import AbstractUser


class Normaluser(AbstractUser):

    username = models.CharField(max_length=64, unique=True,
                                verbose_name='사용자명')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    password = models.CharField(max_length=64, unique=True,
                                verbose_name='비밀번호')
    
    
    class Meta:
        db_table = 'Cooluser'