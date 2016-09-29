# encoding: utf-8
from django.db import models

from nepal.models.container import Container


class Expedition(models.Model):
    """
    """
    name = models.CharField(max_length=40)
    container = models.ManyToManyField(Container,
                                       related_name='expedition',
                                       db_table='expedition_has_container',
                                       null=True,
                                       blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'expedition'
        verbose_name = 'Expedition'
