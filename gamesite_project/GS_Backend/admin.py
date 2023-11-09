from django.contrib import admin
from .models import Game, LeaderboardEntry

# Register your models here.
admin.site.register(LeaderboardEntry)
admin.site.register(Game)