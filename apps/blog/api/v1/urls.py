from django.urls import path, include
from .views import CategoryListAPIView, CategoryRetrieveAPIView, BlogListAPIView, BlogRetrieveAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view()),
    path('articles/', BlogListAPIView.as_view()),
    path('article/<int:pk>/', BlogRetrieveAPIView.as_view()),
]
