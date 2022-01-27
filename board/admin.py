from django.contrib import admin
from .models import Post, Category, Notice


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'pin',
        'content',
        'created_at',
        'file_upload',
        'author',
    )


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Notice)
admin.site.register(Category, CategoryAdmin)
