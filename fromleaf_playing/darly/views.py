from django.shortcuts import get_object_or_404, render

from fromleaf_playing.common.views import PlayingCommonListView, PlayingCommonTemplateView

from fromleaf_playing.darly.models import DarlyPhoto

class DarlyMainView(PlayingCommonTemplateView):
    template_name = 'darly/darly_main.html'


class DarlyPhotoView(PlayingCommonListView):
    template_name = 'darly/photo_album.html'
    context_object_name = 'darly_photo_list'
    
    def get_queryset(self):
        return DarlyPhoto.objects.using('darly').all()

