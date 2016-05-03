from django.shortcuts import render
from django.conf import settings

from fromleaf_common.utils import database as db
from fromleaf_common.views import TemplateCommonView
from fromleaf_common.utils.database import UserData, CompanyData

class AboutMeView(TemplateCommonView):
    
    template_name = 'fromleaf_aboutme/aboutme.html'
    
    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data(**kwargs)
        user_data = UserData(settings.USER_EMAIL)
        company_data = CompanyData(settings.USER_EMAIL)
        
        introduce_comment_list = db.get_simple_comment_list(self, user_data.get_member_info())
        
        context['simple_comment_list'] = introduce_comment_list
        context['site_user_extra_info'] = user_data.get_extra_user_info()
        context['education_list'] = user_data.get_user_education_info()
        context['company_list'] = company_data.get_company_list()
        
        return context