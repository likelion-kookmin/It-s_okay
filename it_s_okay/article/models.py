from django.db import models
from django.utils import timezone
from category.models import Large_category, Medium_category, Small_category
from django.contrib.auth import get_user_model
from user.models import *


class Article(models.Model): 
    writer = models.ForeignKey('user.Normaluser',on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=100, verbose_name='제목')
    category = models.CharField(max_length=20,  default=1, verbose_name='카테고리')
    # category = models.ForeignKey(Category, verbose_name='카테고리', null=True, blank=True, on_delete=models.CASCADE)
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
    board = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    text = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.author.username if self.author else "무명")+ "의 댓글"    

# class Comment(models.Model):
#     writer = models.ForeignKey('user.Normaluser',on_delete=models.CASCADE, verbose_name='댓글 작성자')
#     body = models.CharField(max_length=200, verbose_name='댓글 본문')
#     comment = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='댓글 작성자')
#     create_date = models.DateTimeField()
#     modify_date = models.DateTimeField(null=True, blank=True)
    
#     def __str__(self) -> str:
#         return self.body
    
#     class Meta:
#         db_table = 'cool_board_comment'
#         verbose_name = '쿨괜 게시판_댓글'
#         verbose_name_plural = '쿨괜 게시판_댓글'

# class Comment(models.Model):
#     board = models.ForeignKey('article.Article', on_delete=models.CASCADE, related_name='comments', default=1)
#     author = models.CharField(max_length=200, default=1)
#     text = models.TextField(default=1)
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)

#     def approve(self):
#         self.approved_comment = True
#         self.save()

#     def __str__(self):
#         return self.text
    
#     class Meta:
#         db_table = 'cool_board_comment'
#         verbose_name = '쿨괜 게시판_댓글'
#         verbose_name_plural = '쿨괜 게시판_댓글'

# class Comment(models.Model):
#     post = models.ForeignKey(Article, on_delete = models.CASCADE, default="")
#     user = models.ForeignKey(Normaluser, on_delete = models.CASCADE, default="")
#     textfield = models.TextField(default="")

#     def __str__(self):
#         return self.text
    
#     class Meta:
#         db_table = 'cool_board_comment'
#         verbose_name = '쿨괜 게시판_댓글'
#         verbose_name_plural = '쿨괜 게시판_댓글'


