from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Article
from .forms import BoardForm

# class PublicPostIndexView(generic.ListView): 
#     """게시글의 목록을 표시한다.""" 
#     model = Post

# def board(request):
#     return render(request, 'index/board.html')

def board_list(request):
    boards = Article.objects.all().order_by('-id')
    return render(request, 'index/board_list.html', {"boards" : boards})

def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            # user_id = request.session.get('user')
            
            board = Article()
            board.title = form.cleaned_data['title']
            board.area = form.cleaned_data['area']
            board.headcount = form.cleaned_data['headcount']
            board.kakao_url = form.cleaned_data['kakao_url']
            board.body = form.cleaned_data['body']

            board.save()
            return redirect('/board/list/')
    else :
        form = BoardForm()
    
    return render(request, 'index/board_write.html', {'form' : form})

def board_detail(request, pk):
    board = Article.objects.get(pk=pk)

    return render(request, 'index/board_detail.html', {'board':board})


"""2가지 def funcion = fbv class = cvb"""
"""일단은 함수로""" 