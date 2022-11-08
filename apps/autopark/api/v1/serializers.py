from rest_framework import serializers
from apps.autopark.models import Category, Car, CarImages


class CategoryCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class CarImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = ('id', 'get_image_url')


class CarSerializer(serializers.ModelSerializer):
    car_images = CarImagesSerializer(many=True)

    class Meta:
        model = Car
        fields = (
            'id',
            'title',
            'category',
            'description',
            'car_weight',
            'car_length',
            'car_images'
        )
