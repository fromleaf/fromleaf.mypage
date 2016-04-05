from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # context['object_list'] = ['profile']
        return context

    template_name = 'fromleaf_home/home.html'

   
