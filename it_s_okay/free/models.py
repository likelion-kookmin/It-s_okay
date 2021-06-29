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

class Comment(models.Model):
    board = models.ForeignKey(Free, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='free_comments')
    text = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.author.username if self.author else "무명")+ "의 댓글"    
