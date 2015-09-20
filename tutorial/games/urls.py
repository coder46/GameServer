from django.conf.urls import url
from games import views

urlpatterns = [
    url(r'^games/$', views.games_list),
    url(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
    url(r'^games/search/(?P<pk>[_a-zA-Z0-9]+)/$', views.game_search),
    url(r'^games/homescreen/topgames/$', views.topgames),
    url(r'^games/homescreen/newgames/$', views.newgames),
    url(r'^games/homescreen/banners/$', views.banners),
]
