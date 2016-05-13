from django.shortcuts import render
from django.conf import settings

from fromleaf_common.utils import database as db
from fromleaf_common.utils.database import UserData
from fromleaf_common.views import TemplateCommonView, ListCommonView
from fromleaf_playing.ourhockey.models import Player

class OurHockeyView(TemplateCommonView):
    
    template_name = 'ourhockey/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(OurHockeyView, self).get_context_data(**kwargs)
        context['ourhockey_menu_list'] = ['player_list', 'insert_player', 'search_player', ]
        return context
    
    
class PlayerListView(ListCommonView):
    
    template_name = 'ourhockey/player_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)
        
        return context