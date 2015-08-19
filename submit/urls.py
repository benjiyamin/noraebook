__author__ = 'MillerB'

from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /submit/
    url(r'^submit/$', views.index),
    # ex: /submit/thanks/
    url(r'^submit/thanks/$', views.thanks),
]