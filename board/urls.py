from django.urls import path, include
from . import views
app_name = 'board'

urlpatterns = [
    path('1/', views.notice, name='notice'),
    path('article/<int:article_id>/', views.article_detail, name='detail'),
    path('<int:board_id>/write/', views.article_write, name='write'),
]
