from django.contrib import admin
from django.urls import path, include
import main.urls
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("main/", include(main.urls)),
]
