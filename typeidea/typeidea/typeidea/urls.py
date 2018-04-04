# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from blog.api import PostViewSet, CategoryViewSet, TagViewSet, UserViewSet
from comment.views import CommentView
from config.views import LinkView
from typeidea.custom_site import custom_site
from blog.views import IndexView, CategoryView, TagView, PostView, AuthorView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'categorie', CategoryViewSet)
router.register(r'tag', TagViewSet)
router.register(r'user', UserViewSet)

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
                  url(r'^api/', include(router.urls)),
                  url(r'^api/docs/', include_docs_urls(title='typeidea apis')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                      url(r'^silk/', include('silk.urls', namespace='silk')),
                  ] + urlpatterns
