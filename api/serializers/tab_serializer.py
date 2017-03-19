from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import tab_model

class TabSerializer(serializers.HyperlinkedModelSerializer):
	
	# def get_user(self,request):

	# 	user = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.filter(user=request.user), source='user')
	class Meta:
		model = tab_model.Tab
		fields = (
			'user',
			'artist_url',
			'chords_url',
			'tab_url',
			'artist_name',
			'song_title',
			'album',
			'spotify_track_id',
			'youtube_video_id',
		)
		# depth = 1
