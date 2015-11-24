from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('title', 'content', 'photo')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ('message',)
