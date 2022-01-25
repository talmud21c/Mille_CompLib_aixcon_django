from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Notice


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'pin', 'content', 'file_upload']

class NoticeList(ListView):
    model = Notice
    ordering = '-pk'


class NoticeDetail(DetailView):
    model = Notice