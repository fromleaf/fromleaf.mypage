from django.shortcuts import render

from fromleaf_common.utils import database as db
from fromleaf_common.views import TemplateCommonView

# TEMP_DATA: 나중에 지워야 함.
USER_EMAIL = 'fromleaf@gmail.com'

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
        
        user_member_info = db.get_current_member_info(USER_EMAIL)
        site_user_info = db.get_current_user_info(user_member_info)
        site_user_extra_info = db.get_current_user_extra_info(user_member_info)
        page_info = db.get_current_page_info(self, user_member_info)
        comment_list = db.get_simple_comment_list(self, user_member_info)
        opening_page_info = comment_parser(comment_list[0].comment)
        
        context['page_info'] = page_info
        context['site_user_info'] = site_user_info
        context['site_user_extra_info'] = site_user_extra_info
        context['opening_headding'] = comment_list[0].title.split('.', maxsplit=1)
        context['opening_page_info'] = opening_page_info
        
        return context