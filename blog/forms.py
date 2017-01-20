from django import forms
from .models import Post, Contributor, Page
from django.contrib.auth.models import User

class ContributorForm(forms.ModelForm):

    class Meta:
        model = Contributor
        fields = ('homepage',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'abstract', 'content', 'tags',)

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ('title', 'content')
