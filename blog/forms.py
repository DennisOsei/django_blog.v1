from django import forms
from .models import Post              # means from models file import Post class

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title", "text",)