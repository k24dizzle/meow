from django.conf.urls import url
from . import views

urlpatterns = [
    # home page ex: /
    url(r'^$', views.nba_list, name='nba_list'),
    # scores ex: score/
    url(r'^score/(?P<game_id>[0-9]+)/$', views.score, name='score'),
    # Team ex: CLE/
    url(r'(?P<team>[A-Z]{2,3})/$', views.team, name='team'),
    url(r'(?P<team>[A-Z]{2,3})map/$', views.maps, name='maps')
]

