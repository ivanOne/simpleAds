from django.conf.urls import include, url
from django.contrib import admin

from views import AdsDetail, AdsList

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", AdsList.as_view(), name="ads_list"),
    url(r"^(?P<pk>\d+)$", AdsDetail.as_view(), name="ads_detail")
]
