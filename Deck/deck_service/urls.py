from django.conf.urls import url, include
from deck_service import views

list_deck = views.ViewDeck.as_view({
    'get': 'list',
    })

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/v1/match-deck/', list_deck)
]

