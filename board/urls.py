from django.urls import path, include
from . import views
app_name = 'board'

urlpatterns = [
    path('notice/', views.notice, name='notice'),
    path('article/<int:article_id>/', views.article_detail, name='detail'),

]
