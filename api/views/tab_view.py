from  django.contrib.auth.models import User
from api.serializers import tab_serializer
from api.models import tab_model
# from rest_framework import viewsets
from rest_framework import generics
import json

class TabViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = tab_serializer.TabSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return tab_model.Tab.objects.filter(user=user)


    def post(self, request):
        """
        Purpose: Register a user
        Author: @rtwhitfield84
        """

        # data = request.POST
        req_body = json.loads(request.body.decode())
        new_tab = tab_model.Tab.objects.create(
            user=request.user,
            artist_url=req_body['artist_url'],
            chords_url=req_body['chords_url'],
            tab_url=req_body['tab_url'],
            artist_name=req_body['artist_name'],
            song_title=req_body['song_title'],
            album=req_body['album'],
            spotify_track_id=req_body['spotify_track_id'],
            youtube_video_id=req_body['youtube_video_id'],
            )

# class TabViewSet(viewsets.ModelViewSet):
# 	"""
# 	API endpoint that allows tabs to be viewed
# 	"""
# 	serializer_class = tab_serializer.TabSerializer

# 	def get_queryset(self):
# 		user = self.request.user
# 		print("USEEEEEEEEEER:   ", user)
# 		queryset = user.tab_set.all() 

# 		return queryset