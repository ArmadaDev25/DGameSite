from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LBEntrySerializer
from .models import LeaderboardEntry

# Create your views here.

# Backend Api Views
class LBEntryView(viewsets.ModelViewSet):
    serializer_class = LBEntrySerializer
    queryset = LeaderboardEntry.objects.all()


