# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

from comment.form import CommentForm


class CommentView(TemplateView):
    template_name = 'comment/result.html'

    def get(self, request, *args, **kwargs):
        return super(CommentView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # TODO, 获取 path
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            succeed = True
        else:
            succeed = False

        context = {
            'succeed': succeed,
            'form': comment_form,
        }
        return self.render_to_response(context)
