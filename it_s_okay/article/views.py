from django.shortcuts import render
from .models import Post

# class PublicPostIndexView(generic.ListView): 
#     """게시글의 목록을 표시한다.""" 
#     model = Post

def article(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

"""2가지 def funcion = fbv class = cvb"""
"""일단은 함수로""" 