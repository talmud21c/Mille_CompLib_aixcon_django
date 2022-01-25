from django.contrib import admin
from .models import Post, Category, Notice, Postinstance


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'pin', 'content', 'created_at', 'updated_at', 'file_upload', 'author']

    def pin(self, obj):
        return obj.pin > 0

    pin.short_description = '고정글 설정'
    pin.boolean = True

    pass

# admin.site.register(Post)



class PostInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status')

admin.site.register(Postinstance)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Notice)
admin.site.register(Category, CategoryAdmin)