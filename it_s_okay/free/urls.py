from django.urls import path
from . import views

app_name = 'free'

urlpatterns = [
     path('free_list', views.free_list, name="free_list"),
     path('free_write', views.free_write, name="free_write"),
     path('<int:free_id>', views.free_detail, name="free_detail"),
     path('<int:free_id>/edit/', views.free_edit,name='free_edit'),
     path('<int:free_id>/delete/', views.free_delete,name='free_delete'),
     #path('create',views.create, name="create"),

]
