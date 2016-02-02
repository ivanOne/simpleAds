# -*- coding: utf-8 -*-
__author__ = 'Ivan Kazionov'
from django.views.generic import ListView, DetailView
from .models import Ads, AdsCounter


class AdsList(ListView):
    model = Ads
    template_name = "ads_list.html"


class AdsDetail(DetailView):
    model = Ads
    template_name = "ads_detail.html"

    def get_context_data(self, **kwargs):
        context = super(AdsDetail, self).get_context_data(**kwargs)
        context["count_views"] = self.count_check()
        return context

    def count_check(self):
        if self.request.session.session_key is None:
            self.request.session.save()

        user = self.request.user
        session_key = self.request.session.session_key
        qs = AdsCounter.objects.filter(ads=self.object)

        hit = AdsCounter(session=session_key, ads=self.object)

        if user.is_authenticated():
            if not qs.filter(user=user, ads=self.object):
                hit.user = user
                hit.save()
        else:
            if not qs.filter(session=session_key, ads=self.object):
                hit.save()
        return self.object.get_count_views()