# coding: utf-8
from django import forms


class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label="是否删除", required=False)
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)

    def clean_status(self):
        if self.cleaned_data['status']:
            return 3
        else:
            return 1
