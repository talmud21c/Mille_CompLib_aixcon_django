from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('write/', views.PostCreate.as_view(), name='post_write'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('setFixPost/', views.PostTopFix.as_view(), name='post_topFix'),
    path('notice/', views.NoticeList.as_view(), name='notice_list'),
    path('notice/<int:pk>/', views.NoticeDetail.as_view(), name='notice_detail'),
    path('notice/write/', views.NoticeCreate.as_view(), name='notice_write'),
    path('notice/<int:pk>/update/', views.NoticeUpdate.as_view(), name='notice_update'),
    path('notice/<int:pk>/delete/', views.NoticeDelete.as_view(), name='notice_delete'),
    path('notice/setFixNotice/', views.NoticeTopFix.as_view(), name='notice_topFix'),
]
