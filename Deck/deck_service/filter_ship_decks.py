from number_transformer import NumberTransformer
from models import Deck


class FilterShipDeck(object):
    """
    Get object by deck and ship
    """

    @classmethod
    def get_decks(cls, name, ship):
        names = NumberTransformer.transform(name)

        if type(names) is not int:
            deck_obj = Deck.objects.all()
            for name in names:
                deck_obj = deck_obj.filter(name__icontains=name, ship=ship)
        else:
            deck_obj = Deck.objects.filter(name__icontains=names, ship=ship)

        if not deck_obj.exists():
            deck_obj = Deck.objects.filter(name='Other')

        return deck_obj

