# -*- coding: utf-8 -*-
__author__ = 'Ivan Kazionov'

from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Ads(models.Model):
    title = models.CharField(u"Название", max_length=100)
    description = models.TextField(u"Описание")

    def get_count_views(self):
        return self.counter_hits.all().count()

    class Meta:
        verbose_name = u"Объявление"
        verbose_name_plural = u"Объявления"


class AdsCounter(models.Model):
    ads = models.ForeignKey(Ads, related_name="counter_hits")
    session = models.CharField(max_length=40, editable=False)
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, editable=False)


