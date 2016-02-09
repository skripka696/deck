from rest_framework import serializers
from deck_service import models


class ShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ship
        field = ['pk', 'description']


class DeckSerializer(serializers.ModelSerializer):
    description = serializers.CharField(source='ship.description')

    class Meta:
        model = models.Deck
        fields = ('pk', 'name', 'sort_order', 'description')