from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Normaluser

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
            normaluser = Normaluser(
                username=username,
                password=password
            )

            normaluser.save()
            return render(request, 'main/home.html', res_data)


    return render(request, 'user/register.html', res_data)

def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not(username and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            normaluser = Normaluser.objects.get(username=username)
            if check_password(password, normaluser.password):
                request.session['user'] = normaluser.id
                return redirect('/')

            else:
                res_data['error'] = '비밀번호를 틀렸습니다.'
        
        return render(request, 'user/login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

        return redirect('/')
