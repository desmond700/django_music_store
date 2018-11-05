from django.contrib import admin
from django.contrib.auth.models import Group
from store.models import Music

class MusicAdmin(admin.ModelAdmin):
    list_display = ['song_title', 'artist', 'song_url', 'genre', 'created']
    list_filter = ['created']

admin.site.register(Music, MusicAdmin)
admin.site.unregister(Group)