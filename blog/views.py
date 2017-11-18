# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from .models import Blog, Comment
from django.http import Http404
from .forms import CommentForm


def get_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog-detail.html', ctx)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        ctx = {
            'blogs' : blogs
        }
        return render(request, "blog-list.html", ctx)

def main_site(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        ctx = {
            'blogs' : blogs
        }
        return render(request, "main-site.html", ctx)