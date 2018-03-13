# coding: utf-8
from django import forms


class PostAdminForm(forms.ModelForm):
    # TODO: 处理布尔类型字段
    status = forms.BooleanField(label="是否删除", required=True)

    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
