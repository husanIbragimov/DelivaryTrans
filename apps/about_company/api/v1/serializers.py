from rest_framework import serializers
from apps.about_company.models import AboutCompany, AboutCompanyImages


class AboutCompanyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompanyImages
        fields = (
            'id', 'image'
        )


class AboutCompanySerializer(serializers.ModelSerializer):
    about_images = AboutCompanyImagesSerializer(many=True)

    class Meta:
        model = AboutCompany
        fields = (
            'id',
            'title',
            'description',
            'about_images',
        )
