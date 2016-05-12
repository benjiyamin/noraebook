__author__ = 'MillerB'

from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /login/
    url(r'^login/$', views.login_view, name='login'),
    # ex: /signup/
    url(r'^signup/$', views.signup_view),
    # ex: /logout/
    url(r'^logout/$', views.logout_view),
    # ex: /logout/success/
    url(r'^logout/success/$', views.logout_success),
]