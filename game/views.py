from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import GamesSerializer
from .models import Games

class GamesList(generics.ListCreateAPIView):
    queryset = Games.objects.all().order_by('id')
    serializer_class = GamesSerializer

class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all().order_by('id')
    serializer_class = GamesSerializer