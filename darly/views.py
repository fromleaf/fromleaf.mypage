from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from darly.models import DarlyPhoto

class DarlyPhotoListView(ListView):
    template_name = 'darly/darly_photo_list.html'
    context_object_name = 'darly_photo_list'
    
    def get_queryset(self):
        return DarlyPhoto.objects.all()