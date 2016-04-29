"""fromleaf URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, url

from fromleaf_playing import views as playing_views
from fromleaf_playing.darly import views as darly_views


urlpatterns = [
    url(r'^$', playing_views.PlayingView.as_view(), name='playing_page'),
    url(r'^darly/$', darly_views.DarlyView.as_view(), name='darly_page'),
]