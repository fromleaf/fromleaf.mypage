from django.shortcuts import get_object_or_404, render

from fromleaf_common.views import ListCommonView

from fromleaf_playing.darly.models import DarlyPhoto

class DarlyView(ListCommonView):
    template_name = 'darly/darly.html'
    context_object_name = 'darly_photo_list'
    
    def get_queryset(self):
        return DarlyPhoto.objects.using('darly').all()