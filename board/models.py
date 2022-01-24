from django.db import models
from django.contrib.auth.models import User
import os


# 카테고리
# class Category(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
#
#     def __str__(self):
#         return self.name


# 고정글
class Fixedpost(models.Model):
    pin = models.BooleanField()


#사보 게시판
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #고정글
    #fixed_post = models.ForeignKey()

    # [pk]title
    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/board/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


# 공지사항
#class Notice(models.Model):
    # 제목
    # 카테고리
    # 글 내용
    # 작성일
    # 수정시 수정된 날짜 업데이트
    # 파일 업로드
    # 작성자
    # 고정글