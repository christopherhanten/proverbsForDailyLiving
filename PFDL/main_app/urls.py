# main_app/urls.py
from django.conf.urls import url
from views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^about/$', about),
    url(r'^prayerlist/$', prayerlist),
    url(r'^tenents/$', tenents),
    url(r'^profile/$', profile),
    url(r'^userproverbs/$', userproverbs),
    url(r'^login/$', login),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
]
