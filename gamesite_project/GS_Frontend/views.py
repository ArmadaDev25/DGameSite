from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from GS_Backend.models import Game

# Create your views here.

def home(request):
    games = Game.objects.all()
    print(games)
    return render(request, 'home.html', {
        'game' : games,
        
    })
    

def about(request):
    return render(request, 'about.html')

class GameList(ListView):
    model = Game

class GameDetail(DetailView):
    model = Game

class GlistingCreate(CreateView):
    model = Game
    fields = {'name', 'developer', 'shrt_des', 'long_des', 'genre', 'gameurl'}
    


    
    
   
