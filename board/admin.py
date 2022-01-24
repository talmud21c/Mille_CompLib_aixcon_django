from django.contrib import admin
from .models import Post, Category, Notice


admin.site.register(Post)
admin.site.register(Notice)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)