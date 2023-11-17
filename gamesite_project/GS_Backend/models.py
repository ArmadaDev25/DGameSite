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

    # Bools for determining if the game listing will be displayed in other places around the site
    



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'pk':self.id})


# Model that will attach to each game that determines the various tags
class GameTags(models.Model):
    tagname = models.CharField(max_length=25)

    # Tags list will be attached to a specific game
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=None, related_name="devtags")
    def __str__(self):
        return self.name


class LeaderboardEntry(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField()

    # Leaderboard entries need to be attached to a specific game
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=1, related_name="entry")

    def __str__(self):
        return self.name
