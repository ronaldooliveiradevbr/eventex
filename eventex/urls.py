from django.conf.urls import include, url
from django.contrib import admin

from eventex.core.views import home, speaker_detail, talk_list
from eventex.subscriptions import urls

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^inscricao/', include(urls, namespace='subscriptions')),
    url(r'^palestras/$', talk_list, name='talk_list'),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', speaker_detail, name='speaker_detail'),
]
