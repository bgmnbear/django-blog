# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from comment.views import CommentView
from config.views import LinkView
from typeidea.custom_site import custom_site
from blog.views import IndexView, CategoryView, TagView, PostView, AuthorView
from ckeditor_uploader import urls as uploader_urls

# from config.views import links

urlpatterns = [
                  url(r'^$', IndexView.as_view(), name="index"),
                  url(r'^category/(?P<category_id>\d+)/', CategoryView.as_view(), name="category"),
                  url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag"),
                  url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="detail"),
                  url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name="author"),
                  url(r'^links/$', LinkView.as_view(), name="links"),
                  url(r'^comment/$', CommentView.as_view(), name="comment"),
                  url(r'^admin/', admin.site.urls),
                  url(r'^cus_admin/', custom_site.urls),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
