from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import tab_model
from api.serializers import user_serializer
from rest_framework.fields import CurrentUserDefault

class TabSerializer(serializers.HyperlinkedModelSerializer):
	# user = serializers.PrimaryKeyRelatedField(many=True)
	user = user_serializer.UserSerializer(many=True)
	# user = serializers.HiddenField(
	#     default=serializers.CurrentUserDefault()
	# )


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
			'spotify_album_id',
			'youtube_video_id',
			'art_url',
		)
	def create(self, validated_data):
		user_data = validated_data.pop('user')
		tab = tab_model.Tab.objects.create(**validated_data)
		tab.user.add(self.request.user)

		return tab