from django import forms
from .models import User, Post

class UserForm(forms.UserForm):

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