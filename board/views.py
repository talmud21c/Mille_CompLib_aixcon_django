from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Notice


class PostList(ListView):
    model = Post
    paginate_by = 15
    template_name = 'board/post_list.html'
    context_object_name = 'post_list'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('board:post_list')


class PostSetFix(ListView):
    model = Post
    paginate_by = 5
    template_name = 'board/post_set_fix.html'
    ordering = '-pk'
    fields = ['pin', 'pk', 'title', 'created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 상단고정
        post_fixed = Post.objects.filter(pin=True).order_by('-pk')
        context['post_fixed'] = post_fixed

        return context


class NoticeList(ListView):
    model = Notice
    template_name = 'board/notice_list.html'
    context_object_name = 'notice_list'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 상단고정
        notice_fixed = Notice.objects.filter(pin=True).order_by('-pk')
        context['notice_fixed'] = notice_fixed

        return context


class NoticeDetail(DetailView):
    model = Notice


class NoticeCreate(CreateView):
    model = Notice
    template_name = 'board/notice_write.html'
    fields = ['title', 'category', 'file_upload', 'pin', 'content']


class NoticeEdit(UpdateView):
    model = Notice
    template_name = 'board/notice_write.html'
    fields = ['title', 'category', 'file_upload', 'pin', 'content']


class NoticeDelete(DeleteView):
    model = Notice
    success_url = reverse_lazy('board:notice_list')
