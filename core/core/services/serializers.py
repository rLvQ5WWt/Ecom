from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import Group, User
from django.db import transaction
from rest_framework import serializers






class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)

        # Set the first name and last name
        user.first_name = self.validated_data.get("first_name", "")
        user.last_name = self.validated_data.get("last_name", "")
        user.save()
        # Add the user to the "Student" group
        group, _ = Group.objects.get_or_create(name="Customer")
        user.groups.add(group)
        user.save()

        return user
