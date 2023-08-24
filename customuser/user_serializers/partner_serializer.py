from rest_framework import serializers

from customuser.models import CustomUser


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'id')
