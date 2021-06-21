from django.urls import path
from . import views



app_name = 'article'

urlpatterns = [
    path('list/', views.board_list, name='board_list'),
    path('write/', views.board_write, name='board_write'),
    path('<int:id>/', views.board_detail,name='board_detail'),
    path('<int:id>/edit/', views.board_edit,name='board_edit'),
    path('<int:id>/delete/',views.board_delete,name="board_delete"),
    
]
