from django.shortcuts import render
from .models import Post


def index(request):
    # 쿼리 날려서 온 결과(역순으로)
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'board/index.html',
        {
            # 쿼리 날려서 온 결과를 딕셔너리 형태로 저장
            'posts': posts,
        }
    )