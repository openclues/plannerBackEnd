from rest_framework import generics
# Create your views here.
from rest_framework.permissions import IsAuthenticated

from customuser.user_serializers.serializer import MeUserSerializer


class UserApiView(generics.RetrieveUpdateDestroyAPIView):  # get && update && remove user

    serializer_class = MeUserSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_object(self):
        return self.request.user  # Retrieve the current authenticated user

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()  # Soft delete or deactivate the user instead of hard deleting
