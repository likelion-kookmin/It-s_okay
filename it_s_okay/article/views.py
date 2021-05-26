from django.shortcuts import render
from .models import Post

class PublicPostIndexView(generic.ListView): 
    """게시글의 목록을 표시한다.""" 
    model = Post
