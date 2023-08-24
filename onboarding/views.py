from django.shortcuts import render
from rest_framework import generics
from .models import Onboarding
# Create your views here.
from onboarding.serializer import OnBoardingSerializer


class GetOnBoarindListApiView(generics.ListAPIView):
    serializer_class = OnBoardingSerializer
    queryset = Onboarding.objects.all()