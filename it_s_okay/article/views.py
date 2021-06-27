from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth import get_user_model
from user.models import Normaluser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt 


# 보드 리스트

def board_list(request):
    all_boards = Article.objects.all().order_by('-id')
    page        = int(request.GET.get('p', 1))
    pagenator   = Paginator(all_boards, 5)
    boards      = pagenator.get_page(page)
    return render(request, 'index/board_list.html', {"boards" : boards})

# 보드 작성

def board_write(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.writer = request.user
            article.save()
            print(article.id)
            return redirect('/board/' + str(article.id))
        
    form = ArticleForm()
    return render(request, 'index/board_write.html', {'form' : form})

# 보드 디테일 / 댓글 생성

def board_detail(request, board_id):
    board = get_object_or_404(Article, id=board_id)
    comments = Comment.objects.filter(board=board_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comments = comment_form.save(commit=False)
            text = comment_form.cleaned_data['text']
            comments.board = board
            comments.created = timezone.now()
            comments.article_id = board_id
            comments.author = request.user
            comments.save()
            print(text)
            return redirect('/board/' + str(board.id))

    else:
        comment_form = CommentForm()

    context={
        'board':board,
        'comments':comments,
        'comment_form':comment_form
    }

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)


    return render(request, 'index/board_detail.html', context)


# 보드 수정

def board_edit(request, board_id):
    board = get_object_or_404(Article, id=board_id)
    if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.cleaned_data)
                board.title = form.cleaned_data['title']
                board.category = form.cleaned_data['category']
                board.area = form.cleaned_data['area']
                board.age = form.cleaned_data['age']
                board.headcount = form.cleaned_data['headcount']
                board.state = form.cleaned_data['state']
                board.body = form.cleaned_data['body']
                board.kakao_url = form.cleaned_data['kakao_url']

                board.save()
                return redirect('/board/'+str(board.id))
            
    else:
        form = ArticleForm(instance = board)

        return render(request, 'index/board_edit.html',{'form':form})

# 보드 삭제

def board_delete(request, board_id):
    board = Article.objects.get(id=board_id)

    if request.method == "POST":
        board.delete()
        return redirect('/board/list')   
    
    return render(request, 'index/board_delete.html')



# 댓글 수정

def comment_edit(request, board_id, comment_id):
    board = get_object_or_404(Article, id=board_id)
    comments = Comment.objects.filter(board=board_id)
    my_comment = Comment.objects.get(id=comment_id)
    comment_form = CommentForm(instance=my_comment)

    if request.method == "POST":
        update_comment_form = CommentForm(request.POST, instance=my_comment)
        if update_comment_form.is_valid():
            update_comment_form.save()

            # comments = comment_form.save(commit=False)
            # print(comment_form.cleaned_data)
            # comments.text = comment_form.cleaned_data['text']
            # comments.save()
            return redirect('/board/'+str(board.id))
    # else:
    #     comment_form = CommentForm()
    
    context={
        'board':board,
        'comments':comments,
        'comment_form':comment_form,
        'my_comment':my_comment,
    }
    return render(request, 'index/board_detail_comment_edit.html', context)

# 댓글 삭제

def comment_delete(request, board_id, comment_id):
    board = Article.objects.get(id=board_id)
    comment = Comment.objects.get(id=comment_id)

    if request.user != comment.author :
        messages.warning(request, '권한없음')
        return redirect('/board/'+str(board.id))
    
    if request.method == "POST":
        comment.delete()
        return redirect('/board/'+str(board.id))
    
    
    context={
        'comment':comment
    }
    return render(request, 'index/board_detail_comment_delete.html',context)




