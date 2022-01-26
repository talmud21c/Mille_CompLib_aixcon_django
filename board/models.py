from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import os


# 사보 게시판
class Post(models.Model):
    # 게시글 제목
    title = models.CharField(max_length=50, verbose_name='제목')
    # 고정글
    pin = models.BooleanField(verbose_name='고정글', default=False)
    # 글 내용
    content = RichTextField(blank=True, null=True, verbose_name='내용')
    # 작성일(작성된 날짜 자동 등록)
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 시 수정된 날짜 새로 생성
    updated_at = models.DateTimeField(auto_now=True)
    # 파일 업로드
    file_upload = models.FileField(upload_to='board/files/%Y/%m/%d/', blank=True, verbose_name='파일')
    # 작성자
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='작성자')

    def __str__(self):
        return f'[{self.pin}] [{self.pk}] {self.title} - {self.author}'

    def get_absolute_url(self):
        return f'/board/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


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
    # 고정글

    # 카테고리
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    # 글 내용
    content = RichTextField(blank=True, null=True)
    # 작성일
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정시 수정된 날짜 업데이트
    updated_at = models.DateTimeField(auto_now=True)
    # 파일 업로드
    file_upload = models.FileField(upload_to='board/files/%Y/%m/%d/', blank=True)
    # 작성자
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] [{self.category}] {self.title} - {self.author}'

    def get_absolute_url(self):
        return f'/notice/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]