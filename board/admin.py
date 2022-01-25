from django.contrib import admin
from .models import Post, Category, Notice, Postinstance



admin.site.register(Post)



class PostInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status')

admin.site.register(Postinstance)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Notice)
admin.site.register(Category, CategoryAdmin)