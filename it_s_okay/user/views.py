from django.shortcuts import render

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = re

    return render(request, 'user/register.html')
