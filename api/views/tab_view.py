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



    def post(self, request):
        """
        Purpose: Post a tab
        Author: @rtwhitfield84
        """
        user = self.request.user
        print("@@@@@@@@@@@@@@@@@@@@@@@",user)
        sys.stdout.flush()
        # queryset = tab_model.Tab.objects.filter(user=user)

        req_body = json.loads(request.body.decode())
        tab_model.Tab.objects.create(
            user=user,
            artist_url=req_body['artist_url'],
            chords_url=req_body['chords_url'],
            tab_url=req_body['tab_url'],
            artist_name=req_body['artist_name'],
            song_title=req_body['song_title'],
            album=req_body['album'],
            spotify_track_id=req_body['spotify_track_id'],
            spotify_album_id=req_body['spotify_album_id'],
            youtube_video_id=req_body['youtube_video_id'],
            art_url=req_body['art_url'],
            )
