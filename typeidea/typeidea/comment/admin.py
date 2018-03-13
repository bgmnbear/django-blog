# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from comment.models import Comment
from typeidea.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'content', 'nickname',
                    'website', 'email', 'created_time'
                    ]

    def save_model(self, request, obj, form, change):
        obj.owner = request.user

        return super(CommentAdmin, self).save_model(request, obj, form, change)
