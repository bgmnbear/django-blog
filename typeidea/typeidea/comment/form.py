# coding: utf-8

from __future__ import unicode_literals

from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('字数不足, 请认真回复!')
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
