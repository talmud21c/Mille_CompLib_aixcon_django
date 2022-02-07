from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.BoardList.as_view(), name='board_list'),
    path('write/', views.BoardCreate.as_view(), name='board_write'),
    path('<int:pk>/', views.BoardDetail.as_view(), name='board_detail'),
    path('<int:pk>/update/', views.BoardUpdate.as_view(), name='board_update'),
    path('<int:pk>/delete/', views.BoardDelete.as_view(), name='board_delete'),
    path('setFixPost/', views.BoardTopFix.as_view(), name='board_topFix'),
    path('notice/', views.NoticeList.as_view(), name='notice_list'),
    path('notice/<int:pk>/', views.NoticeDetail.as_view(), name='notice_detail'),
    path('notice/write/', views.NoticeCreate.as_view(), name='notice_write'),
    path('notice/<int:pk>/update/', views.NoticeUpdate.as_view(), name='notice_update'),
    path('notice/<int:pk>/delete/', views.NoticeDelete.as_view(), name='notice_delete'),
    path('notice/setFixNotice/', views.NoticeTopFix.as_view(), name='notice_topFix'),
]
