from rest_framework import generics
from apps.blog.models import Category, Blog, BlogImages
from .serializers import CategorySerializer, BlogSerializer, BlogImagesSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer


class BlogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

