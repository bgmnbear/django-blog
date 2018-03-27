# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from blog.models import Post, Tag, Category
from comment.form import CommentForm
from comment.models import Comment
from comment.views import CommentShowMixin
from config.models import SideBar


class CommonMixin(object):
    def get_category_context(self):
        categories = Category.objects.filter(status=1)

        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)
        return {
            'nav_cates': nav_cates,
            'cates': cates,
        }

    def get_context_data(self, **kwargs):

        side_bars = self.get_side_bars()
        recently_posts = self.get_recently_posts()
        hot_posts = self.get_hot_posts()
        recently_comments = self.get_recently_comments()

        kwargs.update({
            'side_bars': side_bars,
            'recently_comments': recently_comments,
            'recently_posts': recently_posts,
        })
        kwargs.update(self.get_category_context())
        return super(CommonMixin, self).get_context_data(**kwargs)

    def get_recently_comments(self):
        return Comment.objects.filter(status=1)[:10]

    def get_hot_posts(self):
        return Post.objects.filter(status=1).order_by('views')[:10]

    def get_recently_posts(self):
        return Post.objects.filter(status=1)[:10]

    def get_side_bars(self):
        return SideBar.objects.filter(status=1)


class BasePostsView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = True


class IndexView(BasePostsView):
    def get_queryset(self):
        qs = super(IndexView, self).get_queryset()
        query = self.request.GET.get('query')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)


class CategoryView(BasePostsView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostsView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []

        posts = tag.posts.all()
        return posts


class AuthorView(BasePostsView):
    def get_queryset(self):
        qs = super(AuthorView, self).get_queryset()
        author_id = self.kwargs.get('author_id')
        print('a_id', author_id)
        if author_id:
            qs = qs.filter(owner_id=author_id)
        return qs


class PostView(CommonMixin, CommentShowMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
