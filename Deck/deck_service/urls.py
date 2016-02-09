from django.conf.urls import url, include
from django.contrib import admin
from deck_service import views

list_note = views.ViewDeck.as_view({
    'get': 'list',
    'post':'create'
    })


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'deck/$', list_note)
]
