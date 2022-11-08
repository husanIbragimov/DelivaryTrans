from django.urls import path
from .views import AboutCompanyListAPIView, AboutCompanyRetrieveAPIView

urlpatterns = [
    path('about-company/', AboutCompanyListAPIView.as_view()),
    path('about-company/<int:pk>/', AboutCompanyRetrieveAPIView.as_view())
]
