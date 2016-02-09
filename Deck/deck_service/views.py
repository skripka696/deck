from django.shortcuts import render
from rest_framework import viewsets
from models import Ship, Deck
from serializers import DeckSerializer

# Create your views here.

class ViewDeck(viewsets.ModelViewSet):

    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

