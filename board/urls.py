from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('write/', views.PostCreate.as_view(), name='post_write'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('notice/', views.NoticeList.as_view(), name='notice_list'),
    path('notice/<int:pk>/', views.NoticeDetail.as_view(), name='notice_detail'),
]
