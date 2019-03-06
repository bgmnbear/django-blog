# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from config.models import Link, SideBar
from typeidea.custom_site import custom_site


@admin.register(Link, site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(admin.ModelAdmin):
    pass
