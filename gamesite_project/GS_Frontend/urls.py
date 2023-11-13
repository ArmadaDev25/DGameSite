from django.urls import path
from GS_Frontend import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.GameList.as_view(template_name="game_list.html"), name='game_list'),
    path('games/<int:pk>/', views.GameDetail.as_view(template_name="game_pages/game_details.html"), name='game_detail')
]