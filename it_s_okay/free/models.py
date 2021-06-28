from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from user.models import *


class Free(models.Model):
    writer = models.ForeignKey('user.Normaluser',on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    

    def __str__(self):
         return self.title

    class Meta:
        db_table = '자유게시판'

        verbose_name = '자유게시판'
        verbose_name_plural = '자유게시판'
