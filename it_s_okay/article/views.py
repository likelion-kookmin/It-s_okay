from django.shortcuts import render, redirect
from .models import Article
from .forms import BoardForm

# class PublicPostIndexView(generic.ListView): 
#     """게시글의 목록을 표시한다.""" 
#     model = Post

# def board(request):
#     return render(request, 'index/board.html')

def post(request):
    return render(request, 'post.html')

def board_list(request):
    boards = Article.objects.all().order_by('-id')
    return render(request, 'index/board_list.html', {"boards" : boards})

def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            user_id = request.session.get('user')
            
            board = Article()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']

            board.save()
            return redirect('/board/list/')
    else :
        form = BoardForm()
    
    return render(request, 'index/board_write.html', {'form' : form})


"""2가지 def funcion = fbv class = cvb"""
"""일단은 함수로""" 