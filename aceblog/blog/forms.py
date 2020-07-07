from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Comment

class CommentForm(forms.ModelForm):
    commentimg = forms.ImageField(required=False)
    class Meta:
        model = Comment
        fields = ('text','commentimg','microtext')