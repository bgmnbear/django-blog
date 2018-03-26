# coding: utf-8

from __future__ import unicode_literals

from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    target = forms.CharField(max_length=100, widget=forms.widgets.HiddenInput)
    content = forms.CharField(
        label="内容",
        max_length=100,
        widget=forms.widgets.Textarea(attrs={'rows': 6, 'cols': 80, })
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('字数不足, 请认真回复!')
        return content

    class Meta:
        model = Comment
        fields = ['target', 'nickname', 'email', 'website', 'content']
