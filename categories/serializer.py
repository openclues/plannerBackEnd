from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from customuser.user_serializers.partner_serializer import PartnerSerializer
from tasks.models import Task
from tasks.serializer import TaskSerializer
from .models import Category


class CategoriesSerializers(serializers.ModelSerializer):
    shared_with = PartnerSerializer(many=True, read_only=True)
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_tasks(self, obj):
        category = ContentType.objects.get(app_label="categories", model="category")
        tasks = Task.objects.filter(content_type=category, object_id=obj.id)

        return TaskSerializer(tasks, many=True).data
