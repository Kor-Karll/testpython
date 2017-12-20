from django.conf.urls import url
from blog2.views import *

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    url(r'^archive/$', PostDV.as_view(), name='post_archive'),
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive')
]
