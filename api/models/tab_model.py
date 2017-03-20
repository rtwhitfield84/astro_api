from django.contrib.auth.models import User
from django.db import models

class Tab(models.Model):
	"""
		Tab table maintains relevant information to tab
		@rtwhitfield84
	"""
	user = models.ManyToManyField(User)
	artist_url = models.CharField(max_length=128, blank=True)
	chords_url = models.CharField(max_length=128, blank=True)
	tab_url = models.CharField(max_length=128, blank=True)
	artist_name = models.CharField(max_length=128, blank=True)
	song_title = models.CharField(max_length=128, blank=True)
	album = models.CharField(max_length=128, blank=True)
	spotify_track_id = models.CharField(max_length=128, blank=True)
	spotify_album_id = models.CharField(max_length=128, blank=True)
	youtube_video_id = models.CharField(max_length=128, blank=True)
	art_url = models.CharField(max_length=128, blank=True)

	class Meta:
		verbose_name_plural = 'Tabs'

	def __str__(self):
		return '{}: {}'.format(self.artist_name, self.song_title)