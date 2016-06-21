from django.shortcuts import get_object_or_404, render

from fromleaf_playing.common.views import PlayingCommonListView

from fromleaf_playing.darly.models import DarlyPhoto

class DarlyView(PlayingCommonListView):
    template_name = 'darly/main.html'
    context_object_name = 'darly_photo_list'
    
    def get_queryset(self):
        return DarlyPhoto.objects.using('darly').all()
