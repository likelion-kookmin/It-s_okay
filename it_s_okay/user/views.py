from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Normaluser
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

# 회원가입 대안버전

# @csrf_exempt 
# def register(request):
#     if request.method == "POST":
#         if request.POST["password"] == request.POST["re_password"]:
#             normaluser = Normaluser.objects.create_user(
#                 username=request.POST["username"],password=request.POST["password"]
#             )
#             auth.login(request, normaluser)
#             return redirect('user/login.html')
#         return render(request, 'user/register.html')
#     return render(request, 'user/register.html')


#회원가입 초기버전 

@csrf_exempt 
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']

        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = "모든 값을 입력해야합니다."
        elif password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다'
        else:
            normaluser = Normaluser.objects.create_user(
                username=username,
                password=password
            )

            normaluser.save()
            return render(request, 'main/home.html', res_data)


    return render(request, 'user/register.html', res_data)

# # 로그인 대안버전

@csrf_exempt 
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        normaluser = auth.authenticate(request, username=username, password=password)
        
        if normaluser is not None:
            auth.login(request, normaluser)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'error':'아이디 혹은 비밀번호가 다릅니다.'})

    else:
        return render(request, 'user/login.html')

# 로그인 초기버전

# @csrf_exempt 
# def login(request):
#     if request.method == 'GET':
#         return render(request, 'user/login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)

#         res_data = {}
#         if not(username and password):
#             res_data['error'] = '모든 값을 입력해야합니다.'
#         else:
#             normaluser = Normaluser.objects.get(username=username)
#             if check_password(password, normaluser.password):
#                 request.session['user'] = normaluser.id
#                 return redirect('/')

#             else:
#                 res_data['error'] = '비밀번호를 틀렸습니다.'
        
#         return render(request, 'user/login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def mypage(request):
    return render(request, "user/mypage.html")
