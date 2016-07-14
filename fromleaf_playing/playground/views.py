from django.shortcuts import get_object_or_404, render

from fromleaf_playing.common.views import PlayingCommonTemplateView, PlayingCommonFormView


class PlaygroundMainView(PlayingCommonTemplateView):
    template_name = 'playground/playground_main.html'

    def get_context_data(self, **kwargs):
        context = super(PlaygroundMainView, self).get_context_data(**kwargs)
        return context


class PlaygroundWebCrawlerView(PlayingCommonTemplateView):
    template_name = 'playground/crawler.html'
