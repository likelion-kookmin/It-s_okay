from django.contrib import admin
from django.urls import path, include
from main import views
import main.urls
from article import views
import article.urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main.views.index),
    path("main/", include(main.urls)),
    path("board/", include(article.urls)),
]
