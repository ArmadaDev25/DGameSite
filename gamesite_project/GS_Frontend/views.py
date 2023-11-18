from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from GS_Backend.models import Game

# User Login/Registration Imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Registration Views
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Signup'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

    


    
    
   
