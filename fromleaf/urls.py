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
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('fromleaf_opening.urls', namespace='opening')),
    url(r'^aboutme/', include('fromleaf_aboutme.urls', namespace='aboutme')),
    url(r'^myskill/', include('fromleaf_myskill.urls', namespace='myskill')),
#     url(r'^$', PortfolioView.as_view(), name='portfolio'),
#     url(r'^$', ContactMeView.as_view(), name='contactme'),
    url(r'^darly/', include('darly.urls', namespace='darly')),
    url(r'^admin/', admin.site.urls),
]


# TODO: 개발용인데, STATIC 경로가 있어야 하나? Azure에서 없으면 못읽으려나??
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # While I'm developing my site, Media files are saved on "/app_name/media/location".  
    # If I want to laod my media files, I have to use this code.
    urlpatterns += static(r'^(?P<path>.*)$', document_root=settings.MEDIA_ROOT)


