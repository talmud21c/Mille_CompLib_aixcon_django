from django.db import models


class Post(models.Model):
    # 게시글 제목
    title = models.CharField(max_length=50)
    # 글 내용
    content = models.TextField()
    # 작성일(작성된 날짜 자동 등록)
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 시 수정된 날짜 새로 생성
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자
    # author

    # [pk]title
    def __str__(self):
        return f'[{self.pk}] {self.title}'