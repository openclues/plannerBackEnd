from rest_framework import serializers

from customuser.user_serializers.partner_serializer import PartnerSerializer
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    shared_with = PartnerSerializer(many=True, read_only=True)
    who_has_to_make = PartnerSerializer(many=True, read_only=True)
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_content_type(self, obj):
        if obj.content_type:
            return obj.content_type.model
        else:
            return None
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     return {key: value for key, value in data.items() if value is not None}
