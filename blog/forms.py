from django import forms
from .models import CommentPost

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ('text',)