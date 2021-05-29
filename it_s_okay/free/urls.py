from django.urls import path
from . import views

app_name = 'free'

urlpatterns = [
    path('', views.FreeListView.as_view(), name='free_list'),
]
