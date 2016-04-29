from django.shortcuts import render

from fromleaf_common.views import TemplateCommonView

class PlayingView(TemplateCommonView):
    template_name = 'fromleaf_playing/playing.html'
    
    def get_context_data(self, **kwargs):
        context = super(PlayingView, self).get_context_data(**kwargs)
        
        return context