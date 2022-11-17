from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from apps.order.models import Order
from .serializers import OrderSerializer, OrderCreateSerializer

from apps.account.api.v1.permissions import IsOwnUserOrReadOnly, IsAuthenticated


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwnUserOrReadOnly,)


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsOwnUserOrReadOnly,)


class OrderRetrieveAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'transaction_id'
