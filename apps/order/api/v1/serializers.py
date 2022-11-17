from rest_framework import serializers

from apps.autopark.api.v1.serializers import CarSerializer
from apps.order.models import Weight_cargo, Volume_cargo, Type_cargo, Mode_cargo, Order


class WeightCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight_cargo
        fields = '__all__'


class VolumeCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume_cargo
        fields = '__all__'


class TypeCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_cargo
        fields = '__all__'


class ModeCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode_cargo
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'transaction_id',
            'title',
            'user',
            'from_here',
            'to_here',
            'phone_number',
            'weight_cargo',
            'volume_cargo',
            'type_cargo',
            'mode_cargo',
            'date_created',
            'car',
            'image_1',
            'image_2',
            'image_3',
        )


class OrderGETSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    weight_cargo = WeightCargoSerializer()
    volume_cargo = VolumeCargoSerializer()
    type_cargo = TypeCargoSerializer()
    mode_cargo = ModeCargoSerializer()

    class Meta:
        model = Order
        fields = (
            'transaction_id',
            'title',
            'from_here',
            'to_here',
            'phone_number',
            'weight_cargo',
            'volume_cargo',
            'type_cargo',
            'mode_cargo',
            'date_created',
            'car',
            'image_1',
            'image_2',
            'image_3',
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'transaction_id',
            'user',
            'car',
            'title',
            'date_created',
            'from_here',
            'to_here',
            'phone_number',
            'weight_cargo',
            'volume_cargo',
            'type_cargo',
            'mode_cargo',
            'image_1',
            'image_2',
            'image_3',
        )
