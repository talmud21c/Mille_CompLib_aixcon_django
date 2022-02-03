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
        context = super(PostList, self).get_context_data(**kwargs)
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


class PostUpdate(UpdateView):
    model = Post
    template_name = 'board/post_write.html'
    fields = ['title', 'file_upload', 'pin', 'content']


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('board:post_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class PostTopFix(ListView):
    model = Post
    paginate_by = 5
    template_name = 'board/post_top_fix.html'
    ordering = '-pk'
    fields = ['pin', 'pk', 'title', 'created_at']

    def get_context_data(self, **kwargs):
        context = super(PostTopFix, self).get_context_data(**kwargs)
        # 상단고정
        post_fixed = Post.objects.filter(pin=True).order_by('-pk')
        context['post_fixed'] = post_fixed

        return context


class NoticeList(ListView):
    model = Notice
    template_name = 'board/notice_list.html'
    context_object_name = 'notice_list'
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NoticeList, self).get_context_data(**kwargs)
        # 상단고정
        notice_fixed = Notice.objects.filter(pin=True).order_by('-pk')
        context['notice_fixed'] = notice_fixed
        return context


class NoticeDetail(DetailView):
    model = Notice


class NoticeCreate(CreateView):
    model = Notice
    template_name = 'board/notice_write.html'
    fields = ['category', 'title', 'file_upload', 'pin', 'content']


class NoticeUpdate(UpdateView):
    model = Notice
    template_name = 'board/notice_write.html'
    fields = ['category', 'title', 'file_upload', 'pin', 'content']


class NoticeDelete(DeleteView):
    model = Notice
    success_url = reverse_lazy('board:notice_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class NoticeTopFix(ListView):
    model = Notice
    paginate_by = 5
    template_name = 'board/notice_top_fix.html'
    ordering = '-pk'
    fields = ['pin', 'pk', 'category', 'title', 'created_at']

    def get_context_data(self, **kwargs):
        context = super(NoticeTopFix, self).get_context_data(**kwargs)
        # 상단고정
        notice_fixed = Notice.objects.filter(pin=True).order_by('-pk')
        context['notice_fixed'] = notice_fixed

        return context
