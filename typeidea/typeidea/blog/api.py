# coding: utf-8
from rest_framework import routers, serializers, viewsets

from blog.models import Post, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'url', 'name',
            'created_time',
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=1)
    serializer_class = CategorySerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'url', 'title',
            'desc', 'category',
            'created_time',
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
