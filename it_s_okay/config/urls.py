from django.contrib import admin
from django.urls import path, include
from main import views
import main.urls
from article import views
import article.urls
from free import views
from django.conf.urls.static import static
from django.conf import settings






urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main.views.index),
    path("main/", include(main.urls)),
    path("board/", include('article.urls',namespace='board')),
    path("free/", include('free.urls', namespace='free')),
    path("user/", include("user.urls")),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)