from django.shortcuts import render

from fromleaf_playing.common.views import PlayingCommonTemplateView

class PlayingView(PlayingCommonTemplateView):
    template_name = 'fromleaf_playing/playing.html'
