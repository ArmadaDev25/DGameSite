from django.urls import path
from GS_Frontend import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.GameList.as_view(template_name="game_list.html"), name='game_list'),
    path('games/<int:pk>/', views.GameDetail.as_view(template_name="game_pages/game_details.html"), name='game_detail'),
    
    # User Registration URLS
    path('accounts/signup', views.signup, name='signup'),

    # Game Posting URLS
    path('postnewgame/', views.GlistingCreate.as_view(template_name="game_pages/game_form.html"), name='game_form'),
    
    # Built in site Features for games
    path('games/<int:pk>/lb/', views.GameDetail.as_view(template_name="game_pages/game_lb.html"), name='game_lb') #Online Leaderboard Feature Path
]