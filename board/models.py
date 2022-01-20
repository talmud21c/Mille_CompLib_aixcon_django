from django.db import models
import os

class Post(models.Model):
    # 게시글 제목
    title = models.CharField(max_length=50)

    # 글 내용
    content = models.TextField()

    # 작성일(작성된 날짜 자동 등록)
    created_at = models.DateTimeField(auto_now_add=True)

    # 수정 시 수정된 날짜 새로 생성
    updated_at = models.DateTimeField(auto_now=True)

    # 이미지 업로드
    image_upload = models.ImageField(upload_to='board/images/%Y/%m/%d/', blank=True)

    # 파일 업로드
    file_upload = models.FileField(upload_to='board/files/%Y/%m/%d/', blank=True)
    # 작성자
    # author

    # 카테고리
    # category

    # [pk]title
    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/board/{self.pk}/'

    def get_image_name(self):
        return os.path.basename(self.image_upload.name)

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]