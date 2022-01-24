from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Notice


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post


class NoticeList(ListView):
    model = Notice
    ordering = '-pk'


class NoticeDetail(DetailView):
    model = Notice


# def index(request):
#     # 쿼리 날려서 온 결과(역순으로)
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'board/index.html',
#         {
#             # 쿼리 날려서 온 결과를 딕셔너리 형태로 저장
#             'posts': posts,
#         }
#     )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'board/single_page.html',
#         {
#             'post': post,
#         }
#     )