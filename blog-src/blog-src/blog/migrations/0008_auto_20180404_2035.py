# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-04 12:35
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180331_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u5185\u5bb9'),
        ),
    ]
