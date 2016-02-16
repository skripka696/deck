from __future__ import unicode_literals

from django.db import models


class Ship(models.Model):
    name = models.CharField(max_length=25)
    wieght = models.FloatField()
    capacity = models.IntegerField()
    year = models.IntegerField()
    description = models.CharField(max_length=250, default='')

    def __unicode__(self):
        return '{0}'.format(self.name)


class Deck(models.Model):
    name = models.CharField(max_length=25)
    sort_order = models.IntegerField()
    ship = models.ForeignKey(Ship)
    image_link = models.CharField(max_length=255, default='http://image.com')

    def __unicode__(self):
        return '{0}'.format(self.name)
