from django.urls import path
from django_filters.views import FilterView
from . import views



app_name = 'article'

urlpatterns = [
    path('list/', views.board_list, name='board_list'),
    # path('list/', FilterView.as_view(
    #                 filterset_class = UserFilter,
    #                 template_name = 'index/board_list.html'),
    #                 name = 'board_list'),
    path('write/', views.board_write, name='board_write'),
    path('<int:id>/', views.board_detail,name='board_detail'),
    path('<int:id>/edit/', views.board_edit,name='board_edit'),
    path('<int:id>/update/', views.board_update,name="board_update"),
    path('<int:id>/delete/',views.board_delete,name="board_delete"),
    
]
