from django.contrib import admin
from django.urls import path, include
from main import views
import main.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("main/", include(main.urls)),
]
