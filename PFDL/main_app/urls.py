from django.conf.urls import url
from views import index
from views import show
from views import post_proverb


urlpatterns = [
    url(r'^$', index),
    url(r'^([0-9]+)/$', show, name = 'show')
    url(r'^post_url/$', post_proverb, name="post_proverb")
]
