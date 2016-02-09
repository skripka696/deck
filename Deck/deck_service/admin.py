from django.contrib import admin
# Register your models here.
from deck_service import models


admin.site.register(models.Deck)
admin.site.register(models.Ship)
