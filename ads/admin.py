# -*- coding: utf-8 -*-
__author__ = 'Ivan Kazionov'
from django.contrib import admin

from .models import Ads

@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ["title", "views_count"]

    def views_count(self, obj):
        return obj.get_count_views()
    views_count.short_description = u'Колличество просмотров'