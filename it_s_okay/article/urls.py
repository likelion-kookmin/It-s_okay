from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('board/', views.board, name='board'),
]