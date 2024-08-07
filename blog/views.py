from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    context_object_name= 'post'     


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = CommentPost.objects.filter(post=self.object)
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user 
            new_comment.save()
            return redirect(post.get_absolute_url())
        return self.get(request, *args, **kwargs)

class CommentCreateView(generic.CreateView):
    model = CommentPost
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.kwargs['pk']})

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
