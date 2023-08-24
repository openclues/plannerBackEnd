from .models import Onboarding
from rest_framework import serializers


class OnBoardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onboarding
        fields = "__all__"
