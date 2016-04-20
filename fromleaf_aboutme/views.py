from django.shortcuts import render

from fromleaf_common.utils import database as db
from fromleaf_common.views import TemplateCommonView


# TEMP_DATA: 나중에 지워야 함.
USER_EMAIL = 'fromleaf@gmail.com'


class AboutMeView(TemplateCommonView):
    
    template_name = 'fromleaf_aboutme/aboutme.html'
    
    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data(**kwargs)
        
        user_member_info = db.get_current_member_info(USER_EMAIL)
        site_user_extra_info = db.get_current_user_extra_info(user_member_info)
        page_info = db.get_current_page_info(self, user_member_info)
        introduce_comment_list = db.get_simple_comment_list(self, user_member_info)
        education_list = db.get_current_user_education_info(user_member_info)
        company_list = db.get_current_user_company_info(user_member_info)
        
        context['simple_comment_list'] = introduce_comment_list
        context['site_user_extra_info'] = site_user_extra_info
        context['education_list'] = education_list
        context['company_list'] = company_list
        
        return context