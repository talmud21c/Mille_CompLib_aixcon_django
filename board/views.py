from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

import board.views
from .models import Post, Notice


class PostList(ListView):
    model = Post
    paginate_by = 15
    template_name = 'board/post_list.html'
    context_object_name = 'post_list'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 페이지네이션
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        # 상단고정
        post_fixed = Post.objects.filter(pin=True).order_by('-pk')
        context['post_fixed'] = post_fixed

        return context


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    template_name = 'board/post_write.html'
    fields = ['title', 'file_upload', 'pin', 'content']


class PostEdit(UpdateView):
    model = Post
    template_name = 'board/post_write.html'
    fields = ['title', 'file_upload', 'pin', 'content']


class NoticeList(ListView):
    model = Notice
    ordering = '-pk'


class NoticeDetail(DetailView):
    model = Notice