from django.db import models
from django.db.models.fields import CharField, IntegerField

class Post(models.Model): 
    STATE = (
        ('ing','모집중'),
        ('complete', '모집완료')
    )
    AGE_STATE = (
        ('ten','10대'),
        ('twenty', '20대'),
        ('third', '30대'),
        ('forty', '40대'),
        ('fifty', '50대 이상'),
    )
    age = models.CharField(max_length=20, choices=AGE_STATE)
    area = models.CharField(max_length=20)
    title = models.CharField('제목',max_length=32)
    text = models.TextField('본문')
    kakao_url = models.CharField('카카오',max_length=200)
    meeting_time = models.DateTimeField('날짜')
    headcount = models.IntegerField('인원수')
    state = models.CharField('상태',max_length=20, choices=STATE)
    created_at = models.DateTimeField('작성일',auto_now_add=True)
    updated_at = models.DateTimeField('갱신일',auto_now=True)

    # TODO : add sort , anonymous
    
    def __str__(self) -> str:
        return self.title

class Comment(models.Model): 
    """게시글에 대한 댓글""" 
    name = models.CharField('이름', max_length=255, default='이름없음')
    text = models.TextField('본문') 
    # target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='대상게시글') 
    created_at = models.DateTimeField('작성일', auto_now_add=True) 

    def __str__(self): 
        return self.text[:20]

class Reply(models.Model): 
    """대댓글""" 
    name = models.CharField('이름', max_length=255, default='이름없음') 
    text = models.TextField('본문') 
    target = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='대상댓글') 
    created_at = models.DateTimeField('작성일', auto_now_add=True) 
    
    def __str__(self): 
        return self.text[:20]


