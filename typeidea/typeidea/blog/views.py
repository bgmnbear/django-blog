# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render

from blog.models import Post, Tag, Category
from comment.models import Comment
from config.models import SideBar


def get_common_context():
    categories = Category.objects.filter(status=1)

    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    side_bars = SideBar.objects.filter(status=1)

    recently_posts = Post.objects.filter(status=1)[:10]
    # hot_posts = Post.objects.filter(status=1).order_by('views')[:10]
    recently_comments = Comment.objects.filter(status=1)[:10]

    context = {
        'nav_cates': nav_cates,
        'cates': cates,
        'side_bars': side_bars,
        'recently_comments': recently_comments,
        'recently_posts': recently_posts,
    }
    return context


def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()

    if category_id:
        queryset = Post.objects.filter(category_id=category_id)
    elif tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()

    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except TypeError:
        page = 1

    page_size = 2
    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    common_context = get_common_context()
    context.update(common_context)
    return render(request, 'blog/list.html', context=context)


def post_detail(request, pk=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    context = {
        'post': post,
    }
    common_context = get_common_context()
    context.update(common_context)
    return render(request, 'blog/detail.html', context=context)
