from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator 
from django.contrib import messages
from django.utils import timezone
from .forms import FreeForm, CommentForm
from .models import Free, Comment
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def free_list(request):
    all_boards = Free.objects.all().order_by('-id')
    page        = int(request.GET.get('p', 1))
    pagenator   = Paginator(all_boards, 5)
    boards      = pagenator.get_page(page)
    return render(request, 'free/free_list.html', {"boards" : boards})
    
    # free_board = Free.objects.all()
    # #return render(request, 'free/free_list.html')
    # return render(request, 'free/free_list.html', {"free_board" : free_board})

def free_detail(request, free_id):
    board = get_object_or_404(Free, id=free_id)
    comments = Comment.objects.filter(board=free_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comments = comment_form.save(commit=False)
            text = comment_form.cleaned_data['text']
            comments.board = board
            comments.created = timezone.now()
            comments.free_id = free_id
            comments.author = request.user
            comments.save()
            print(text)
            return redirect('/free/' + str(board.id))

    else:
        comment_form = CommentForm()


    context={
        'board':board,
        'comments':comments,
        'comment_form':comment_form
    }

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
    # comment = get_object_or_404(Comment, id=board.id)


    return render(request, 'free/free_detail.html', context)

def free_write(request):
    if request.method == 'POST':
        form = FreeForm(request.POST)
        if form.is_valid():
            article_free = form.save(commit=False)
            article_free.writer = request.user
            article_free.save()
        return redirect('/free/'+ str(article_free.id))
        
    form = FreeForm()
    return render(request, 'free/free_write.html', {'form' : form})

def free_edit(request, free_id):
    free_board = get_object_or_404(Free, pk=free_id)
    if request.method == "POST":
            form = FreeForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.cleaned_data)
                free_board.title = form.cleaned_data['title']
                free_board.content = form.cleaned_data['content']


                free_board.save()
                return redirect('/free/'+str(free_board.id))
            
        # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = FreeForm(instance = free_board)

        return render(request, 'free/free_edit.html',{'form':form})

def free_delete(request, free_id):
    free_board = Free.objects.get(pk=free_id)
    free_board.delete()
    
    
    return redirect('/free/free_list')

def comment_edit(request, free_id, comment_id):
    board = get_object_or_404(Free, id=free_id)
    comments = Comment.objects.filter(board=free_id)
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
            return redirect('/free/'+str(board.id))
    # else:
    #     comment_form = CommentForm()
    
    context={
        'board':board,
        'comments':comments,
        'comment_form':comment_form,
        'my_comment':my_comment,
    }
    return render(request, 'free/free_detail_comment_edit.html', context)

def comment_delete(request, free_id, comment_id):
    board = Free.objects.get(id=free_id)
    comment = Comment.objects.get(id=comment_id)

    if request.user != comment.author :
        messages.warning(request, '권한없음')
        return redirect('/free/'+str(board.id))
    
    if request.method == "POST":
        comment.delete()
        return redirect('/free/'+str(board.id))
    
    
    context={
        'comment':comment
    }
    return render(request, 'free/free_detail_comment_delete.html',context)