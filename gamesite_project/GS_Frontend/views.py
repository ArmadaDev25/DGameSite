from django.shortcuts import render
from django.views.generic import ListView
from GS_Backend.models import Game

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class GameList(ListView):
    model = Game
    
    
   
