"""myDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','musics.views.list_all'),

    url(r'^music_create/$','musics.views.music_create'),
    url(r'^musician_create/$','musics.views.musician_create'),
    url(r'^country_create/$','musics.views.country_create'),
    url(r'^musicStyle_create/$','musics.views.musicStyle_create'),
    
    url(r'^music_update/(?P<id>\d+)/$','musics.views.music_update'),
    url(r'^musician_update/(?P<id>\d+)/$','musics.views.musician_update'),
    url(r'^country_update/(?P<id>\d+)/$','musics.views.country_update'),
    url(r'^musicStyle_update/(?P<id>\d+)/$','musics.views.musicStyle_update'),

    url(r'^music_delete/(?P<id>\d+)/$','musics.views.music_delete'),
    url(r'^musician_delete/(?P<id>\d+)/$','musics.views.musician_delete'),
    url(r'^country_delete/(?P<id>\d+)/$','musics.views.country_delete'),
    url(r'^musicStyle_delete/(?P<id>\d+)/$','musics.views.musicStyle_delete'),

    url(r'^music_detail/(?P<id>\d+)/$','musics.views.music_detail'),
    url(r'^musician_detail/(?P<id>\d+)/$','musics.views.musician_detail'),
    url(r'^country_detail/(?P<id>\d+)/$','musics.views.country_detail'),
    url(r'^musicStyle_detail/(?P<id>\d+)/$','musics.views.musicStyle_detail'),
]
