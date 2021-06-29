from django.contrib.auth.hashers import check_password
from django import forms 
from django.forms.models import ModelForm
from .models import Article, Comment





class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','category','area','age','meeting_date','headcount','state','body','kakao_url'] 

        
    abstract=True
    STATE = [
    ("모집중", "모집중"),
    ("모집완료", "모집완료"),
    ]
    AGE_STATE = [
    ("10대", "10대"),
    ("20대", "20대"),
    ("30대", "30대"),
    ("40대", "40대"),
    ("50대 이상", "50대 이상"),
    ]

    CATEGORY = [
    ('--야외 스포츠--',
        (
    ("풋살", "풋살"),
    ("축구", "축구"),
    ("농구", "농구"),
    ("야구", "야구"),
    ("배드민턴", "배드민턴"),
        )
    ),
    ('--문화--',
        (
    ("영화", "영화"),
    ("전시회", "전시회"),
    ("독서모임", "독서모임"),
        )
    ),
    ('--엔터테이먼트--',
        (
    ("방탈출", "방탈출"),
    ("보드게임", "보드게임"),
        )
    ),
    ('--스터디--',
        (
    ("스터디", "스터디"),
        )
    ),
    ('--온라인 활동--',
        (
    ("게임", "게임"),
    ("온라인 스터디", "온라인 스터디"),
        )
    ),             
    ]  

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
    meeting_date = forms.DateField(
        widget = forms.SelectDateWidget,
        label = "만남 희망 날짜",
        error_messages={
            'required': '만남 희망 날짜를 선택해주세요.'
        },
        )
    
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
        widget = forms.Textarea(attrs={'autocomplete':'off'}),
        label = "본문"
    )


    kakao_url = forms.CharField(
        error_messages={
            'required': '만나기를 희망하는 위치를 입력해주세요.'
        },
        label= "오픈 카톡 url"
    )


class CommentForm(forms.ModelForm):
    #text = forms.TextInput(label = '댓글')

    class Meta:
        model = Comment
        fields = ['text']
        # widgets = {
        #     'text': forms.CharField
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['text'].label = "댓글"

    # text = forms.CharField(
    # error_messages={
    #     'required': '댓글을 입력해주세요.'
    # },
    # max_length=50,
    # label = "댓글"
    # )


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['text'].label = "댓글"
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['body']
#         labels = {
#             'body': '댓글내용',
#         }

# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('author', 'text',)