from django.shortcuts import render
from django.conf import settings

from fromleaf_common.utils import database as db
from fromleaf_common.views import TemplateCommonView
from fromleaf_common.utils.database import UserData

def comment_parser(comment):
    comment_dict = {}
    element_list = comment.split(',')
    
    for element in element_list:
        key, value = element.split(':', maxsplit=1)
        comment_dict[key] = value
            
    return comment_dict

class OpeningView(TemplateCommonView):
    
    template_name = 'fromleaf_opening/opening.html'
    
    def get_context_data(self, **kwargs):
        context = super(OpeningView, self).get_context_data(**kwargs)
        user_data = UserData(settings.USER_EMAIL)
        
        comment_list = db.get_simple_comment_list(self, user_data.get_member_info())
        opening_page_info = comment_parser(comment_list[0].comment)
        
        context['site_user_extra_info'] = user_data.get_extra_user_info()
        context['opening_headding'] = comment_list[0].title.split('.', maxsplit=1)
        context['opening_page_info'] = opening_page_info
        
        return context