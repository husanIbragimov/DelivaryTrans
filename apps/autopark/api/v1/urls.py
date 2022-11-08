from django.urls import path
from .views import CategoryListAPIView, CategoryRetrieveAPIView, CarListAPIView, CarRetrieveAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view()),
    path('auto-cars/', CarListAPIView.as_view()),
    path('auto-car/<int:pk>/', CarRetrieveAPIView.as_view())
]
