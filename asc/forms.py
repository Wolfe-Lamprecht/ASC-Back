from django import forms
from .models import User, Post

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'bio',
            'status',
            'picture',
        )

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'body'
        )