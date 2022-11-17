from django.urls import path

from .views import OrderCreateAPIView, OrderListAPIView, OrderRetrieveAPIView

urlpatterns = [
    path('Order-api-view/', OrderListAPIView.as_view()),
    path('Order-api-view/create', OrderCreateAPIView.as_view()),
    path('retrieve/<str:transaction_id>/', OrderRetrieveAPIView.as_view())
    # path('Order-api-view/<int:pk>/', Order_api_view)
]
