from django.urls import path

from eventex.subscriptions.views import new, detail

urlpatterns = [
    path('', new, name='new'),
    path('<int:pk>/', detail, name='detail'),
]
