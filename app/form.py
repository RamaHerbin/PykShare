from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from app.models import Comment, Post


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        content = forms.CharField(max_length=200)

        # widgets = {
        #     'content': forms.Textarea(attrs={'class':'form-control'})
        # }


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image']