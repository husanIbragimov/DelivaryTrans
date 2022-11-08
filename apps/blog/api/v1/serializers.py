from rest_framework import serializers
from apps.blog.models import Category, Blog, BlogImages


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class BlogImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImages
        fields = ('id', 'get_image_url')


class BlogSerializer(serializers.ModelSerializer):
    blog_images = BlogImagesSerializer(many=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'category', 'description', 'blog_images')
