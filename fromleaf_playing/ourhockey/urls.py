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

from fromleaf_playing.ourhockey import views


urlpatterns = [
    url(r'^$', views.OurHockeyMainView.as_view(), name='main'),
    url(r'^member_list/$', views.MemberListView.as_view(), name='member_list'),
    url(r'^game_schedule/$', views.GameScheduleListView.as_view(),
        name='game_schedule'),
    url(r'^game_schedule/updated_gameday/$',
        views.GameScheduleListView.as_view(), name='updated_gameday'),
    url(r'^select_today_attend/$',
        views.SelectTodayAttendListView.as_view(), name='select_today_attend'),
    url(r'^selected_today_attend/$',
        views.SelectedTodayAttendListView.as_view(), name='selected_today_attend'),
    url(r'^today_attended_list/$',
        views.TodayAttendedMemberListView.as_view(), name='today_attended_list'),

    # Example Using Ajax
    url(r'^home/$', views.home, name='home'),
    url(r'^home/create_post/$', views.create_post, name='create_post'),
]
