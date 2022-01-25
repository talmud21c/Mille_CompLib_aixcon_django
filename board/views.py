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