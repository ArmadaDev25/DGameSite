from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=120)
    developer = models.CharField(max_length=120)
    

    def __str__(self):
        return self.name

class LeaderboardEntry(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField()

    # Leaderboard entries need to be attached to a specific game
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
