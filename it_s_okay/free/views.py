from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator 
from .forms import FreeForm
from .models import Free
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
    free_board = get_object_or_404(Free, pk=free_id)

    # comment = get_object_or_404(Comment, id=board.id)


    return render(request, 'free/free_detail.html', {'free_board':free_board})

def free_write(request):
    if request.method == 'POST':
        form = FreeForm(request.POST)
        if form.is_valid():
            article_free = form.save(commit=False)
            # new_free = Free()
            # new_free.title = request.POST['title']
            # new_free.content = request.POST['content']
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

# def create(request):
#     new_free = Free()
#     new_free.title = request.POST['title']
#     new_free.content = request.POST['body']
#     new_free.save()
#     return redirect('free/free_detail'+ str(new_free.id))
