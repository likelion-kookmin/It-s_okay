from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Article
from .forms import ArticleForm
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

# def board_write(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.author = request.user
#             article.save()
#             print(article.id)
#             return redirect('/board/' + str(article.id))
        
#     form = ArticleForm()
#     return render(request, 'index/board_write.html', {'form' : form})

def board_write(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            normaluser = Normaluser.objects.get(pk=user_id)

            article = Article()
            article.title = form.cleaned_data['title']
            article.category = form.cleaned_data['category']
            article.area = form.cleaned_data['area']
            # article.date = form.cleaned_data['date']
            article.age = form.cleaned_data['age']
            article.headcount = form.cleaned_data['headcount']
            article.state = form.cleaned_data['state']
            article.body = form.cleaned_data['body']
            article.kakao_url = form.cleaned_data['kakao_url']
            article.writer = normaluser
            article.save()
            print(article.id)
            return redirect('/board/' + str(article.id))
    
    else :
        form = ArticleForm()
    
    return render(request, 'index/board_write.html', {'form': form})



# 보드 디테일

def board_detail(request, id):
    board = get_object_or_404(Article, id=id)
    form = ArticleForm(instance = board)



    return render(request, 'index/board_detail.html', {'form':form,'board':board})

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
        # context = {
        #     'form' : form,
        #     'writing' : True,
        #     'now' : 'edit',
        # }
        return render(request, 'index/board_edit.html',{'form':form})

# def board_edit(request,id):
#     board = Article.objects.get(id=id)
#     context= {'board': board}
#     return render(request, 'index/board_edit.html', context)


# def board_update(request, id):
#     board = get_object_or_404(Article, id=id)
#     if request.method == "POST":
#         form = ArticleForm(request.POST,instance = board)
#         if form.is_valid():
#             form.save()
#             return redirect('/board/' + str(id))
    
#     else:
#         form = ArticleForm(instance = board)

#         return render(request, 'index/board_edit.html', {'form':form})

# 보드 삭제

def board_delete(request, id):
    board = Article.objects.get(id=id)
    board.delete()
    # messages.success(request, "삭제되었습니다.")
    
    return redirect('/board/list/')


    

