from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Post , CommentPost
from .forms import CommentForm

class PostListView(generic.ListView):
    model= Post
    template_name ='blog/post_list.html'
    context_object_name= 'posts'

    def get_queryset(self):
        return Post.objects.filter(status= True)
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    # context_object_name= 'post'

    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = CommentPost.objects.all()
        return context
    
class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = CommentPost
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)

        form.instance.post = post
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse_lazy('blog:post_detail', kwargs={'pk': post_id})
     

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
    template_name= 'blog/post_create.html'
    fields = ('title', 'text', 'status', 'author',)
