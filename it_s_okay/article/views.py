from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
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




# 보드 디테일

def board_detail(request, id):
    board = get_object_or_404(Article, id=id)
    # comments = Comment.objects.filter(id=id)
    comments = Comment.objects.all()


    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comments = comment_form.save(commit=False)
            text = comment_form.cleaned_data['text']
            comments.comment_user = request.user
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
    # form_class = CommentForm
    # form = form_class(request.POST or None)

    # comment = get_object_or_404(Comment, id=board.id)

    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.author = request.user
    #         comment.save()
    #         return redirect('/board/' + str(board.id))

    return render(request, 'index/board_detail.html', context)


# 보드 수정
def board_edit(request, id):
    board = get_object_or_404(Article, id=id)
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
            
        # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = ArticleForm(instance = board)

        return render(request, 'index/board_edit.html',{'form':form})



# 보드 삭제

def board_delete(request, id):
    board = Article.objects.get(id=id)
    board.delete()
    
    
    return redirect('/board/list/')

# def comment(request, board_id):

#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             form.instance.board_id = board_id
#             comment.save()
#             print(board_id)
#             return redirect('/board/' + str(board_id))
    
#     form = CommentForm()              
#     return render(request, 'index/board_detail.html', {'form' : form})

    # return HttpResponseRedirect(reverse_lazy('board:detail', args=[document_id]))

# # get_absolute_url을 설정해 놓았을 시(in models)
#     def get_absolute_url(self):
#         return reverse('board:detail', args=[self.id])

#  제일 마지막 문장    return redirect(document)로  대체가능



# 댓글 생성

# def add_comment_to_board(request, id):
#     board = get_object_or_404(Article, id=id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.board = board
#             comment.save()
#             print(board.id)
#             return redirect('/board/' + str(board.id))
#     else:
#         form = CommentForm()
#     return render(request, 'index/board_detail.html', {'form': form})

# def comment_write(request, id):
#     errors =[]
#     board = Article.objects.get(id=id)


#     if request.method == 'POST':
#         # board_id = request.POST.get('board_id','').strip()
#         content = request.POST.get('content', '').strip()
        
#         # if not content:
#         #     errors.append("댓글을 입력하세요.")
#         if not errors:
#             comment = Comment.objects.create(
#                 user = request.user,
#                 board_id = board.id,
#                 content = content)
#             return redirect('/board/' + str(board.id))

            
#     return render(request, 'board_detail.html', {'user':request.user, 'errors':errors})

    # def board_write(request):
    # if request.method == 'POST':
    #     form = ArticleForm(request.POST)
    #     if form.is_valid():
    #         article = form.save(commit=False)
    #         article.writer = request.user
    #         article.save()
    #         print(article.id)
    #         return redirect('/board/' + str(article.id))
        
    # form = ArticleForm()
    # return render(request, 'index/board_write.html', {'form' : form})


