from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LBEntrySerializer
from .models import LeaderboardEntry

# Create your views here.

# Backend Api Views
# Admin API
class LBEntryViewSet(viewsets.ModelViewSet):
    serializer_class = LBEntrySerializer
    queryset = LeaderboardEntry.objects.all()
    permission_classes = [permissions.IsAuthenticated]


