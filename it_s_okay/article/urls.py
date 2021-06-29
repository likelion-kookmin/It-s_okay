from django.urls import path
from django.conf.urls import url
from . import views



app_name = 'article'

urlpatterns = [
    path('list/', views.board_list, name='board_list'),
    path('write/', views.board_write, name='board_write'),
    path('<int:board_id>/', views.board_detail,name='board_detail'),
    path('<int:board_id>/edit/', views.board_edit,name='board_edit'),
    path('<int:board_id>/delete/',views.board_delete,name="board_delete"),
    path('<int:board_id>/comment_edit/<int:comment_id>',views.comment_edit,name='comment_edit'),
    path('<int:board_id>/comment_delete/<int:comment_id>',views.comment_delete,name='comment_delete'),
    path('category_list/', views.category_list, name='category_list'),




]
