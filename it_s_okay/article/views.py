from django.shortcuts import render, get_object_or_404
from .models import Article

# class PublicPostIndexView(generic.ListView): 
#     """게시글의 목록을 표시한다.""" 
#     model = Post

def board(request):
    return render(request, 'index/board.html')

def post(request):
    return render(request, 'post.html')

"""2가지 def funcion = fbv class = cvb"""
"""일단은 함수로""" 