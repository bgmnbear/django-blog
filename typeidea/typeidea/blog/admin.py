# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from .models import Post, Category, Tag


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    list_display = ['title', 'category', 'status_show', 'owner',
                    'created_time', 'operator'
                    ]
    # list_display_links = ['category']

    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name', 'owner__username']
    save_on_top = True
    show_full_result_count = True

    actions_on_top = True
    actions_on_bottom = False
    date_hierarchy = 'created_time'
    # list_editable = ('title', 'status')

    fieldsets = (

        ('基础配置', {

            'fields': (('category', 'title'),
                       'desc',
                       'status',
                       'content',
                       )

        }),

        ('高级配置', {

            'classes': ('collapse', 'addon'),

            'fields': ('tags',),

        }),

    )
    filter_horizontal = ('tags',)

    def operator(self, obj):
        return format_html(

            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))

        )

    operator.allow_tags = True
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user

        return super(PostAdmin, self).save_model(request, obj, form, change)


class PostInlineAdmin(admin.TabularInline):
    fields = ('title', 'status')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInlineAdmin,
    ]


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass
