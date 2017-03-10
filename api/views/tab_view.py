from  django.contrib.auth.models import User
from api.serializers import tab_serializer
from api.models import tab_model
from rest_framework import viewsets

class TabViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows tabs to be viewed
	"""

	queryset = tab_model.Tab.objects.all() 
	serializer_class = tab_serializer.TabSerializer