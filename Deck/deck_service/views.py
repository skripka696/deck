from rest_framework import viewsets
from models import Deck
from serializers import DeckSerializer
from rest_framework.response import Response
from transform_number import transform


class ViewDeck(viewsets.ModelViewSet):

    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def list(self, request):
        ship = request.GET.get('ship', '0')
        name = transform(request.GET.get('name', 'Other'))

        queryset = Deck.objects.filter(name__icontains=name, ship=ship)
        if not queryset.exists():
            queryset = Deck.objects.filter(name='Other', ship=5)
        serializer = DeckSerializer(queryset, many=True)
        return Response(serializer.data)


