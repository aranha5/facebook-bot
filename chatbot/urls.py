from django.conf.urls import include, url

from .views import SpotifyBotView


urlpatterns = [
    url('^spotify/?$', SpotifyBotView.as_view(), name='spotify'),
]
