from django.db import models
from django.contrib.auth.models import User
import uuid
import os


# 사보 게시판
class Post(models.Model):
    # 게시글 제목
    title = models.CharField(max_length=50)
    # 글 내용
    content = models.TextField()
    # 작성일(작성된 날짜 자동 등록)
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 시 수정된 날짜 새로 생성
    updated_at = models.DateTimeField(auto_now=True)
    # 파일 업로드
    file_upload = models.FileField(upload_to='board/files/%Y/%m/%d/', blank=True)
    # 작성자
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.title} - {self.author}'

    def get_absolute_url(self):
        return f'/board/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


# 사보게시판 고정글
class Postinstance(models.Model):
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    POST_STATUS = (
        (0, 'Nonfixed'),
        (1, 'Fixed'),
    )

    status = models.BooleanField(choices=POST_STATUS, blank=False, default='0')


    class Meta:
        ordering = ['status']

    def __str__(self):
        return f'[{self.post}] -- [{self.post.id}] {self.post.title}'


# 카테고리
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


# 공지사항
class Notice(models.Model):
    # 제목
    title = models.CharField(max_length=50)
    # 카테고리
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    # 글 내용
    content = models.TextField()
    # 작성일
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정시 수정된 날짜 업데이트
    updated_at = models.DateTimeField(auto_now=True)
    # 파일 업로드
    file_upload = models.FileField(upload_to='board/files/%Y/%m/%d/', blank=True)
    # 작성자
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # 고정글

    def __str__(self):
        return f'[{self.pk}] [{self.category}] {self.title} - {self.author}'

    def get_absolute_url(self):
        return f'/notice/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]