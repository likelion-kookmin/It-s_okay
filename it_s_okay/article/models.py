from django.db import models
from category.models import Large_category, Medium_category, Small_category
from django.contrib.auth import get_user_model
from user.models import *


class Article(models.Model): 
    writer = models.ForeignKey('user.Normaluser',on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=100, verbose_name='제목')
    category = models.CharField(max_length=20,  default=1, verbose_name='카테고리')
    area = models.CharField(max_length=20, verbose_name='위치')
    age = models.CharField(max_length=20,  default=1, verbose_name='연령대')
    meeting_date = models.CharField(max_length=20, verbose_name='만남 시간')
    headcount = models.IntegerField(verbose_name='모집인원')
    state = models.CharField(max_length=20,  default=1, verbose_name='모집상태')
    body = models.TextField(verbose_name='내용')
    kakao_url = models.CharField(max_length=200,verbose_name='오픈카톡 url')
    # large_category = models.ForeignKey(Large_category, on_delete=models.SET_NULL, null=True)
    # medium_category = models.ForeignKey(Medium_category, on_delete=models.SET_NULL, null=True)
    # small_category = models.ForeignKey(Small_category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'cool_board'
        verbose_name = '쿨괜 게시판'
        verbose_name_plural = '쿨괜 게시판'
    


class Comment(models.Model):
    writer = models.ForeignKey('user.Normaluser',on_delete=models.CASCADE, verbose_name='댓글 작성자')
    body = models.CharField(max_length=200, verbose_name='댓글 본문')
    comment = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='댓글 작성자')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.body
    
    class Meta:
        db_table = 'cool_board_comment'
        verbose_name = '쿨괜 게시판_댓글'
        verbose_name_plural = '쿨괜 게시판_댓글'


