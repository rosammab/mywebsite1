# my_app/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']  # Adjust based on your Post model fields

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Adjust based on your Comment model fields
