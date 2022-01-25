from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('new_post/', views.PostCreate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('notice/<int:pk>/', views.NoticeDetail.as_view()),
    path('notice/', views.NoticeList.as_view()),
]