from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('write/', views.PostCreate.as_view(), name='post_write'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('notice/<int:pk>/', views.NoticeDetail.as_view()),
    path('notice/', views.NoticeList.as_view()),
]
