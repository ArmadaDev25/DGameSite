from rest_framework import serializers
from .models import LeaderboardEntry

class LBEntrySerializer(serializers.ModelSerializer): # Class that serializes the LeaderboardEntry Model
    class Meta:
        model = LeaderboardEntry
        fields = ('id', 'name', 'score')