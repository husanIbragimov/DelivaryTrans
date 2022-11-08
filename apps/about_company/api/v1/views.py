from rest_framework import generics
from .serializers import AboutCompanySerializer
from apps.about_company.models import AboutCompany


class AboutCompanyListAPIView(generics.ListAPIView):
    queryset = AboutCompany.objects.filter(is_active=True)
    serializer_class = AboutCompanySerializer


class AboutCompanyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer
