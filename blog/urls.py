from django.urls import path

from . import views

app_name= 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('add/', views.PostCreateView.as_view(), name='post_add'),
    path('<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment_create')
]
