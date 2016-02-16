from rest_framework import serializers
from deck_service import models


class DeckSerializer(serializers.ModelSerializer):
    """
    Serializer for deck model
    """
    description = serializers.CharField(source='ship.description')
    deck = serializers.CharField(source='name')

    class Meta:
        model = models.Deck
        fields = ('deck', 'sort_order', 'description')

