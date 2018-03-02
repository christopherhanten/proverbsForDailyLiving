# main_app/urls.py
from django.conf.urls import url
from views import index
from views import show

urlpatterns = [
    url(r'^$', index),
    url(r'^([0-9]+)/$', show, name = 'show')
]
