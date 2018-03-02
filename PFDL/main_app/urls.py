from django.conf.urls import url
from views import index
from views import show
from views import post_proverb


urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/$', about),
    url(r'^results/$', tenets),
    url(r'^profile/$', prayerList),
    url(r'^login/$', login),
    url(r'^profile/$', profile),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
