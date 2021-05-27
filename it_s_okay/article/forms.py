from django.contrib.auth.hashers import check_password

from django import forms
from .models import Article

class BoardForm(forms.Form):
    title = forms.CharField(error_messages={
        'required': '제목을 입력하세요.'
    }, max_length=100, label="게시글 제목")
    body = forms.CharField(error_messages={
        'required': '내용을 입력하세요.'
    }, widget=forms.Textarea, label="게시글 내용")

    # age = forms.CharField(error_messages={
    #     'required': '나이를 입력하세요.'
    # }, max_length=20, choices=AGE_STATE)
    
    area = forms.CharField(error_messages={
        'required': '지역을 입력하세요.'
    }, max_length=20, label = "지역")

    kakao_url = forms.CharField(error_messages={
        'required': '오픈카톡방/카카오톡 아이디를 입력하세요.'
    }, max_length=200, label="오픈카톡방 주소 / 카카오톡 아이디")
    
    meeting_date = forms.DateField(error_messages={
        'required': '만남 희망 날짜를 입력하세요.'
    }, label = "만남 희망 날짜를 입력하세요.")
    # headcount = models.IntegerField()
    # state = models.CharField(max_length=20, choices=STATE)
    # # large_category = models.ForeignKey(Large_category, on_delete=models.SET_NULL, null=True)
    # # medium_category = models.ForeignKey(Medium_category, on_delete=models.SET_NULL, null=True)
    # # small_category = models.ForeignKey(Small_category, on_delete=models.SET_NULL, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)