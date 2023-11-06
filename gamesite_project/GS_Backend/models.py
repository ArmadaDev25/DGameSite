from django.db import models

# Create your models here.
class Game(models.Model):
    gamename = models.CharField(max_length=120)

class LeaderboardEntry(models.Model):
    name = models.CharField(max_lenght=120)
    score = models.IntegerField()

    def __str__(self):
        return self.name
