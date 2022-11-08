from rest_framework import serializers
from apps.contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'title',
            'phone_number',
            'status',
            'description',
            'from_here',
            'to_here'
        )
