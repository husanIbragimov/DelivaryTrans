from rest_framework import generics
from apps.autopark.models import Car, Category
from .serializers import CategoryCarSerializer, CarSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryCarSerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCarSerializer


class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer


class CarRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
