from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import HttpResponse
from django.core import serializers
import json
from api.serializers import user_serializer




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return user_serializer.RestrictedUserSerializer
        return user_serializer.UserSerializer 