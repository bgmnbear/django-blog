# coding: utf-8

from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from blog.models import Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
