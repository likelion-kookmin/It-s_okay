"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
=======
from django.urls import path, include
from main import views
import main.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('main/', include(main.urls)),
>>>>>>> ec3078b2b188f34b99a6210a55c8c7ba3bc40d5c
]
