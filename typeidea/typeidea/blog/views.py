# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

def post_list(request, category_id=None, tag_id=None):
    context = {
        'name': 'post_list',
    }
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    context = {
        'name': 'post_list',
    }
    return render(request, 'blog/detail.html', context=context)
