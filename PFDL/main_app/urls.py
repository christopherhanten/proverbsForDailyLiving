from django.conf.urls import url
from views import index
from views import show
from views import post_proverb


urlpatterns = [
<<<<<<< HEAD
    url(r'^$', index),
    url(r'^([0-9]+)/$', show, name = 'show')
    url(r'^post_url/$', post_proverb, name="post_proverb")
]
=======
    url(r'^$', views.index),
    url(r'^about/$', about),
    url(r'^results/$', tenets),
    url(r'^profile/$', prayerList),
    url(r'^login/$', login),
    url(r'^profile/$', profile),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
>>>>>>> f11cb8af41b467bdc5b8fbbc2264db94d1a5c084
