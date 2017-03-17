from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import tab_model

class TabSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = tab_model.Tab
		fields = (
			'id',
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
