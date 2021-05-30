from django.contrib.auth.hashers import check_password

from django import forms
from django.forms.models import ModelForm
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =[
            'title',
            'category',
            'meeting_date',
            'age',
            'area',
            'headcount',
            'kakao_url',
            'state',
            'body']
        
        # todo : add meetingdate




    


    # state = forms.CharField(error_messages={
    #     'required': '모임 희망 인원을 입력하세요.'
    # }, choices=Article.STATE, max_length=20, label='모집상태')

    # # large_category = models.ForeignKey(Large_category, on_delete=models.SET_NULL, null=True)
    # # medium_category = models.ForeignKey(Medium_category, on_delete=models.SET_NULL, null=True)
    # # small_category = models.ForeignKey(Small_category, on_delete=models.SET_NULL, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)