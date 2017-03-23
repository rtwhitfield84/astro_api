from  django.contrib.auth.models import User
from api.serializers import tab_serializer
from api.models import tab_model
from rest_framework import viewsets
import sys
import json

class TabView(viewsets.ModelViewSet):

    serializer_class = tab_serializer.TabSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = user.tab_set.all()

        return queryset

