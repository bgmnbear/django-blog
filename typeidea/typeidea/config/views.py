# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView

from blog.views import CommonMixin
from comment.form import CommentForm
from config.models import Link


class LinkView(CommonMixin, ListView):
    queryset = Link.objects.filter(status=1)
    template_name = 'config/links.html'
    context_object_name = 'links'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
        })
        return super(LinkView, self).get_context_data(**kwargs)
