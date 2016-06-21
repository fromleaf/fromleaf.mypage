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
from django.conf.urls import patterns, url, include

from fromleaf_playing import views

urlpatterns = [
    url(r'^$', views.PlayingView.as_view(), name='playing_main'),
    url(r'^darly/', include('fromleaf_playing.darly.urls', namespace='darly')),
    url(r'^ourhockey/', include('fromleaf_playing.ourhockey.urls', namespace='ourhockey')),
]