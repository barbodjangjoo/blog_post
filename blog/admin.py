from django.contrib import admin

from .models import Post, CommentPost

class CommentInline(admin.TabularInline):
    model= CommentPost
    fields = ['user', 'post', 'datetime_modified', 'text', ]
    extra = 0
@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    model = Post
    ordering = ('datetime_modified', )

    inlines= [
        CommentInline,
    ]

