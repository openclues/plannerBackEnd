from rest_framework import serializers

from categories.models import Category
from categories.serializer import CategoriesSerializers
from customuser.models import CustomUser
from customuser.user_serializers.partner_serializer import PartnerSerializer
from event.models import Event
from event.serializer import EventSerializers
from tasks.models import Task
from tasks.serializer import TaskSerializer


class MeUserSerializer(serializers.ModelSerializer):
    my_categories = CategoriesSerializers(many=True, source='category_owner')
    my_events = EventSerializers(many=True, source='event_owner')
    shared_with_me = serializers.SerializerMethodField()
    partners = PartnerSerializer(many=True)
    class Meta:
        fields = ('first_name','last_name','id', 'email', 'phone_number', 'pic_image','partners','my_categories','my_events','shared_with_me')  # Use the correct field name
        model = CustomUser

    def get_shared_with_me(self, obj):
        shared_with_me_data = {
            'categories': CategoriesSerializers(Category.objects.filter(shared_with__in=[obj]), many=True).data,
            'events': EventSerializers(Event.objects.filter(shared_with__in=[obj]), many=True).data,
            'tasks': TaskSerializer(Task.objects.filter(shared_with__in=[obj]), many=True).data,
            # Replace with actual shared category data
            # 'events': []       # Replace with actual shared event data
            # Add other shared content types as needed
        }
        return shared_with_me_data
