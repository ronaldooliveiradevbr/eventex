from django.urls import include, path
from django.contrib import admin

from eventex.core.views import home, speaker_detail, talk_list

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('inscricao/', include(('eventex.subscriptions.urls', 'subscriptions'), namespace='subscriptions')),
    path('palestras/', talk_list, name='talk_list'),
    path('palestrantes/<slug:slug>/', speaker_detail, name='speaker_detail'),
]
