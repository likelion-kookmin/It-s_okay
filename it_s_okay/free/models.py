
import os
from django.conf import settings
from django.db import models

class Free(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')


    def __str__(self):
        return self.title

    class Meta:
        db_table = '자유게시판'
        verbose_name = '자유게시판'
        verbose_name_plural = '자유게시판'
