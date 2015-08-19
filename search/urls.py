__author__ = 'MillerB'

from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index),
    # ex: /favorites/
    url(r'^favorites/$', views.favorites),
    # ex: /search/
    url(r'^search/$', views.search),
    # ex: /like/
    url(r'^like/$', views.like),
]