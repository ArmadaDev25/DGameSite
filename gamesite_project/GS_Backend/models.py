from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=120)
    developer = models.CharField(max_length=120, default=None)
    shrt_des = models.CharField(max_length=500, default=None) # Contains the short description for the game to be used on the game card
    long_des = models.CharField(max_length=1200, default=None) # Contains a much longer description of the game for the details page
    genre = models.CharField(max_length=20, default=None)
    gameurl = models.CharField(max_length=50, default=None)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'pk':self.id})

class LeaderboardEntry(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField()

    # Leaderboard entries need to be attached to a specific game
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
