from django.urls import path, include
from .views import ContactListAPIView, ContactCreateAPIView

urlpatterns = [
    path('create/', ContactCreateAPIView.as_view()),
    path('list/', ContactListAPIView.as_view()),
]
