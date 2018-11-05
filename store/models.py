from django.db import models
from django.contrib import admin

# Create your models here.

class Music(models.Model):
    GENRE_CHOICES = (
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('reggae', 'Reggae'),
        ('rock', 'Rock'),
        ('metal', 'Metal'),
        ('alternative', 'Alternative'),
        ('latin', 'Latin'),
        ('disco', 'Disco'),
        ('pop', 'Pop'),
        ('blues', 'Blues')
    )
    song_title = models.CharField(max_length=500, default=None)
    artist = models.CharField(max_length=200, default=None)
    song_url = models.CharField(max_length=1000, default=None)
    genre = models.CharField(max_length=50, choices = GENRE_CHOICES, default=None)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_title