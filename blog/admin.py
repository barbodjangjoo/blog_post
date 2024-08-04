from django.contrib import admin

from .models import Post


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    model = Post
    ordering = ('datetime_modified', )

