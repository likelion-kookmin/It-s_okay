from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Article
from .forms import ArticleForm
from django.contrib.auth import get_user_model




def board_list(request):
    all_boards = Article.objects.all().order_by('-id')
    page        = int(request.GET.get('p', 1))
    pagenator   = Paginator(all_boards, 4)
    boards      = pagenator.get_page(page)
    return render(request, 'index/board_list.html', {"boards" : boards})

def board_write(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            print(article.id)
            return redirect('/board/' + str(article.id))
        
    form = ArticleForm()
    return render(request, 'index/board_write.html', {'form' : form})

def board_detail(request, id):
    board = get_object_or_404(Article, id=id)

    return render(request, 'index/board_detail.html', {'board':board})

def board_edit(request,id):
    board = Article.objects.get(id=id)
    context= {'board': board}
    return render(request, 'index/board_edit.html', context)

def board_update(request, id):
    board = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST,instance = board)
        if form.is_valid():
            form.save()
            return redirect('/board/' + str(id))
    
    else:
        form = ArticleForm(instance = board)

        return render(request, 'index/board_edit.html', {'form':form})

def board_delete(request, id):
    board = Article.objects.get(id=id)
    board.delete()
    # messages.success(request, "삭제되었습니다.")
    
    return redirect('/board/list/')


    

