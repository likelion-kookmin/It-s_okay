from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('list/', views.PublicpostIndexView.as_view(),name='top'),
]