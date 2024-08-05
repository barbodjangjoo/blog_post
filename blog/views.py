from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Post

class PostListView(generic.ListView):
    model= Post
    template_name ='blog/post_list.html'
    context_object_name= 'posts'

    def get_queryset(self):
        return Post.objects.filter(status= True)
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name= 'post'

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name= 'blog/post_update.html'
    fields = ('title', 'text', 'status',)
    success_url = reverse_lazy('blog:post_list')

class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model= Post
    template_name= 'blog/post_delete.html'
    success_url = reverse_lazy('blog:post_list')

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model= Post
    template_name= 'blog/post_update.html'
    fields = ('title', 'text', 'status', 'author',)
    
