__author__ = 'MillerB'

from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /search/
    url(r'^submit/$', views.index),
]