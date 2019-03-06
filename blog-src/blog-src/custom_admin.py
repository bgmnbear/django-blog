# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    针对有 owner 属性的数据, 重写
    1. save_model - 保证每条数据都属于当前用户
    2. 重写 get_queryset - 保证每个用户只能看到自己的文章
    """

    def get_query(self, request):
        qs = super(BaseOwnerAdmin, self).get_quryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
