from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from customuser.user_serializers.partner_serializer import PartnerSerializer
from event.models import Event
from tasks.models import Task
from tasks.serializer import TaskSerializer


class EventSerializers(serializers.ModelSerializer):
    shared_with = PartnerSerializer(many=True, read_only=True)
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_tasks(self, obj):
        event = ContentType.objects.get(app_label="event", model="event")
        tasks = Task.objects.filter(content_type=event, object_id=obj.id)

        return TaskSerializer(tasks, many=True).data
