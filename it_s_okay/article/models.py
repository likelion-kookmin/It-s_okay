from django.db import models
from category.models import Large_category, Medium_category, Small_category

class Post(models.Model): 
    STATE = (
        ('ing','모집중'),
        ('complete', '모집완료')
    )
    AGE_STATE = (
        ("ten", "10대"),
        ("twenty", "20대"),
        ("third", "30대"),
        ("forty", "40대"),
        ("fifty", "50대 이상"),
    )
    age = models.CharField(max_length=20, choices=AGE_STATE)
    area = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    body = models.TextField()
    kakao_url = models.CharField(max_length=200)
    meeting_time = models.DateTimeField()
    headcount = models.IntegerField()
    state = models.CharField(max_length=20, choices=STATE)
    large_category = models.ForeignKey(Large_category, on_delete=models.SET_NULL, null=True)
    edium_category = models.ForeignKey(Medium_category, on_delete=models.SET_NULL, null=True)
    small_category = models.ForeignKey(Small_category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.body[:10]
