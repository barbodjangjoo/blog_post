from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.author}: {self.title}'
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args={self.pk})
    