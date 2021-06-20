from django.contrib.auth.hashers import check_password
from django import forms 
from django.forms.models import ModelForm
from .models import Article





class ArticleForm(forms.Form):
    abstract=True
    STATE = (
    (1, "모집중"),
    (2, "모집완료"),
    )
    AGE_STATE = (
    (1, ("10대")),
    (2, ("20대")),
    (2, ("30대")),
    (2, ("40대")),
    (2, ("50대 이상")),
    )

    CATEGORY = (
    (1, ("풋살")),
    (2, ("축구")),
    (3, ("농구")),
    (4, ("야구")),
    (5, ("배드민턴")),
    )   

    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=128, label="제목")
    category = forms.ChoiceField(
            choices= CATEGORY,
            label= "활동 유형",
            widget=forms.Select(),
            error_messages={
            'required': '활동 유형을 선택해주세요.'
        },
        )
    area = forms.CharField(
        error_messages={
            'required': '만나기를 희망하는 위치를 입력해주세요.'
        },
        max_length=128, label="만남 희망 위치")
    age = forms.ChoiceField(
            choices= AGE_STATE,
            label= "모집 연령대",
            widget=forms.Select(),
            error_messages={
            'required': '모집 연령대를 선택해주세요.'
        },
        )
    # meeting_date = forms.DateField(
    #     widget = forms.SelectDateWidget,
    #     label = "만남 희망 날짜",
    #     error_messages={
    #         'required': '만남 희망 날짜를 선택해주세요.'
    #     },
    #     )

    headcount = forms.IntegerField(
        label= "모집 인원",
        error_messages={
            'required': '모집 인원를 선택해주세요.'
        },
    )
    state = forms.ChoiceField(
            choices= STATE,
            label= "모집 상태",
            widget=forms.Select(),
            error_messages={
            'required': '모집 상태를 선택해주세요.'
        },
        )
    body = forms.CharField(
        error_messages={
            'required': '본문을 입력해주세요.'
        },
        widget = forms.Textarea,
        label = "본문"
    )
    kakao_url = forms.CharField(
        error_messages={
            'required': '만나기를 희망하는 위치를 입력해주세요.'
        },
        label= "오픈 카톡 url"
    )


    #     status = forms.ChoiceField(choices = STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    #     relevance = forms.ChoiceField(choices = RELEVANCE_CHOICES, required=True)
    #     # todo : add meetingdate

    #         title = forms.CharField(
    #     error_messages={
    #         'required': '제목을 입력해주세요.'
    #     },
    #     max_length=128, label="제목")
    # contents = forms.CharField(
    #     error_messages={
    #         'required': '내용을 입력해주세요.'
    #     },
    #     widget=forms.Textarea, label="내용")




    


    # state = forms.CharField(error_messages={
    #     'required': '모임 희망 인원을 입력하세요.'
    # }, choices=Article.STATE, max_length=20, label='모집상태')

    # # large_category = models.ForeignKey(Large_category, on_delete=models.SET_NULL, null=True)
    # # medium_category = models.ForeignKey(Medium_category, on_delete=models.SET_NULL, null=True)
    # # small_category = models.ForeignKey(Small_category, on_delete=models.SET_NULL, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)