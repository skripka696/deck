from rest_framework import viewsets
from models import Deck
from serializers import DeckSerializer
from rest_framework.response import Response
from filter_ship_decks import FilterShipDeck


class ViewDeck(viewsets.ModelViewSet):
    """
    Returns object by deck and ship
    """

    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def list(self, request):
        partial = request.GET.get('partial')
        ship = request.GET.get('ship')
        n = request.GET.get('name')
        queryset = FilterShipDeck.get_deck(ship=ship, name=n)

        if partial:
            serializer = DeckSerializer(queryset, many=True)
        else:
            serializer = DeckSerializer(queryset.first())

        return Response(serializer.data)

