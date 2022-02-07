from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Notice


class BoardList(ListView):
    model = Post
    paginate_by = 15
    template_name = 'board/board_list.html'
    context_object_name = 'board_list'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(BoardList, self).get_context_data(**kwargs)
        # 상단고정
        post_fixed = Post.objects.filter(pin=True).order_by('-pk')
        context['post_fixed'] = post_fixed

        return context


class BoardDetail(DetailView):
    model = Post
    template_name = 'board/board_detail.html'


class BoardCreate(CreateView):
    model = Post
    template_name = 'board/board_write.html'
    fields = ['title', 'file_upload', 'pin', 'content']


class BoardUpdate(UpdateView):
    model = Post
    template_name = 'board/board_write.html'
    fields = ['title', 'file_upload', 'pin', 'content']


class BoardDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('board:board_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# 고정글 설정 페이지
class BoardTopFix(ListView, UpdateView):
    model = Post
    paginate_by = 5
    template_name = 'board/board_top_fix.html'
    ordering = '-pk'
    fields = ['pin', 'pk', 'title', 'created_at']

    def get_context_data(self, **kwargs):
        context = super(BoardTopFix, self).get_context_data(**kwargs)
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
        # 상단 고정
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
