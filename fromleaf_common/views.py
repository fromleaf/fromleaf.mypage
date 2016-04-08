from django.shortcuts import get_object_or_404, render
from django.views.generic import View, TemplateView, DetailView

class SideBarView(TemplateView, template_url):
    
    template_name = template_url
    
    def get_context_data(self, **kwargs):
        context = super(SideBarView, self).get_context_data(**kwargs)
        
        return context