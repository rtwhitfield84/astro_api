from  django.contrib.auth.models import User
from api.serializers import tab_serializer
from api.models import tab_model
from rest_framework import viewsets

class TabViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows tabs to be viewed
	"""
	serializer_class = tab_serializer.TabSerializer

	def get_queryset(self):
		user = self.request.user
		print("USEEEEEEEEEER:   ", user)
		queryset = user.tab_set.all() 

		return queryset