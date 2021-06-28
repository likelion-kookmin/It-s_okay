from django.contrib.auth.hashers import check_password
from django import forms 
from django.forms.models import ModelForm
from .models import Free





class FreeForm(forms.ModelForm):
    class Meta:
        model = Free
        fields = ['title','content'] 

        
    abstract=True
    

    

    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=128, label="제목")
    
    
    content = forms.CharField(
        error_messages={
            'required': '본문을 입력해주세요.'
        },
        widget = forms.Textarea(attrs={'autocomplete':'off'}),
        label = "본문"
    )


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