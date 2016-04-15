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
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import patterns, url

from fromleaf_history import views

urlpatterns = [
    url(r'^$', views.HistoryView.as_view(), name='history_page'),
    url(r'^company_detail/(?P<pk>\d+)/$', views.CompanyDetailView.as_view(), name='company_detail'),
    url(r'^project_detail/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
]