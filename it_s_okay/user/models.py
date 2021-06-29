from django.db import models
from django.contrib.auth.models import AbstractUser


class Normaluser(AbstractUser):

    username = models.CharField(max_length=64, unique=True,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64, 
                                verbose_name='비밀번호')

    def __str__(self):
        return self.username
    
    
    class Meta:
        db_table = 'Cooluser'
        verbose_name = '쿨괜 사용자'
        verbose_name_plural = '쿨괜 사용자'