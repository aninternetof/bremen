from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .models import Page
from .models import Tagline
from .models import Contributor
from .forms import PostForm
from .forms import PageForm
from .forms import ContributorForm
from django.contrib.auth.forms import UserCreationForm
from taggit.models import Tag
import random

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    pages = Page.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'pages': pages})

def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    pages = Page.objects.all()
    return render(request, 'blog/page.html', {'this_page': page, 'pages': pages})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    pages = Page.objects.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'pages': pages})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags__name__in=[tag]).distinct()
    pages = Page.objects.all()
    return render(request, 'blog/tag_detail.html', {'tag': tag, 'posts': posts, 'pages':pages})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    if Tagline.objects.all().exists():
        tagline = random.choice(Tagline.objects.all())
    else:
        tagline = ""
    pages = Page.objects.all()
    return render(request, 'blog/post_edit.html', {'form': form, 'pages': pages})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.author:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                form.save_m2m()
                return redirect('post_detail', slug=post.slug)
        else:
            form = PostForm(instance=post)
        pages = Page.objects.all()
        return render(request, 'blog/post_edit.html', {'form': form, 'pages': pages})
    else:
        return redirect('post_detail', slug=post.slug)

@login_required
def page_new(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.slug = slugify(page.title)
            page.save()
            form.save_m2m()
            return redirect('page', slug=page.slug)
    else:
        form = PageForm()
    pages = Page.objects.all()
    return render(request, 'blog/page_edit.html', {'form': form, 'pages': pages})

@login_required
def page_edit(request, slug):
    post = get_object_or_404(Page, slug=slug)
    if request.method == "POST":
        form = PageForm(request.POST, instance=post)
        if form.is_valid():
            page = form.save(commit=False)
            page.save()
            form.save_m2m()
            return redirect('page', page.slug)
    else:
        form = PageForm(instance=post)
    pages = Page.objects.all()
    return render(request, 'blog/page_edit.html', {'form': form, 'pages': pages})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    pages = Page.objects.all()
    return render(request, 'blog/post_draft_list.html', {'posts': posts, 'pages': pages})

@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('post_detail', slug=slug)

@login_required
def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.author:
        post.delete()
        return redirect('post_list')
    else:
        return redirect('post_detail', slug=post.slug)

@login_required
def page_remove(request, slug):
    page = get_object_or_404(Page, slug=slug)
    page.delete()
    return redirect('post_list')

@login_required
def user_new(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        contributor_form = ContributorForm(request.POST)
        if all([user_form.is_valid(), contributor_form.is_valid()]):
            user = user_form.save(commit=False)
            user.save()
            contributor = contributor_form.save(commit=False)
            contributor.user = user
            contributor.save()
            return redirect('post_list')
    else:
        user_form = UserCreationForm()
        contributor_form = ContributorForm()
    pages = Page.objects.all()
    return render(request, 'blog/user_edit.html', {'user_form': user_form, 'contributor_form': contributor_form, 'pages': pages})
