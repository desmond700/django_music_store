from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from store.models import Music



def home(request):
    return redirect('store')

def store(request):
    return render(request, 'store/store.html')

def player(request, name):
    id = request.GET.get('songid')
    music = Music.objects.get(pk = id)
    musiclist = Music.objects.filter(genre=name)
    return render(request, 'store/music_player.html', 
        { 
            'music': music,
            'music_list': musiclist 
        }
    )

class genre(ListView):
    """Renders the home page, with a list of all messages."""
    model = Music
    context_object_name = 'music_list'
    template_name = 'store/genre.html'

    def get_queryset(self):
        genre = self.kwargs['genre']
        return Music.objects.filter(genre=genre)

    