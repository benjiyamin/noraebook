__author__ = 'MillerB'

from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index),
    # ex: /search/
    url(r'^search/$', views.search),
]