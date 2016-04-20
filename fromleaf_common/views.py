import logging

from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView

from fromleaf_common.utils import database as db

# TEMP_DATA: 나중에 지워야 함.
USER_EMAIL = 'fromleaf@gmail.com'

class TemplateCommonView(TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super(TemplateCommonView, self).get_context_data(**kwargs)
        user_member_info = db.get_current_member_info(USER_EMAIL)
        user_extra_info = db.get_current_user_extra_info(user_member_info)
        user_sns_info_list = db.get_current_user_sns_list_info(user_member_info)
        introduce_comment = db.get_introduce_comment(user_member_info)
        page_info = db.get_current_page_info(self, user_member_info)

        context['meta_user_info'] = user_extra_info
        context['sidebar_user_info'] = user_extra_info
        context['sidebar_user_introduce_comment'] = introduce_comment
        context['sidebar_user_extra_info'] = user_extra_info
        context['sidebar_user_sns_info_list'] = user_sns_info_list
        context['member_info'] = user_member_info
        context['page_info'] = page_info
        
        return context
    
class ListCommonView(ListView):
    
    def get_context_data(self, **kwargs):
        context = super(ListCommonView, self).get_context_data(**kwargs)
        user_member_info = db.get_current_member_info(USER_EMAIL)
        user_extra_info = db.get_current_user_extra_info(user_member_info)
        user_sns_info_list = db.get_current_user_sns_list_info(user_member_info)
        introduce_comment = db.get_introduce_comment(user_member_info)
        page_info = db.get_current_page_info(self, user_member_info)

        context['meta_user_info'] = user_extra_info
        context['sidebar_user_info'] = user_extra_info
        context['sidebar_user_introduce_comment'] = introduce_comment
        context['sidebar_user_extra_info'] = user_extra_info
        context['sidebar_user_sns_info_list'] = user_sns_info_list
        context['member_info'] = user_member_info
        context['page_info'] = page_info
        
        return context
    
    
class FormCommonView(FormView):
    
    def get_context_data(self, **kwargs):
        context = super(FormCommonView, self).get_context_data(**kwargs)
        user_member_info = db.get_current_member_info(USER_EMAIL)
        user_extra_info = db.get_current_user_extra_info(user_member_info)
        user_sns_info_list = db.get_current_user_sns_list_info(user_member_info)
        introduce_comment = db.get_introduce_comment(user_member_info)
        page_info = db.get_current_page_info(self, user_member_info)

        context['meta_user_info'] = user_extra_info
        context['sidebar_user_info'] = user_extra_info
        context['sidebar_user_introduce_comment'] = introduce_comment
        context['sidebar_user_extra_info'] = user_extra_info
        context['sidebar_user_sns_info_list'] = user_sns_info_list
        context['member_info'] = user_member_info
        context['page_info'] = page_info
        
        return context
    
    
class DetailCommonView(DetailView):
    
    def get_context_data(self, **kwargs):
        context = super(DetailCommonView, self).get_context_data(**kwargs)
        user_member_info = db.get_current_member_info(USER_EMAIL)
        user_extra_info = db.get_current_user_extra_info(user_member_info)
        user_sns_info_list = db.get_current_user_sns_list_info(user_member_info)
        introduce_comment = db.get_introduce_comment(user_member_info)
        page_info = db.get_current_page_info(self, user_member_info)

        context['meta_user_info'] = user_extra_info
        context['sidebar_user_info'] = user_extra_info
        context['sidebar_user_introduce_comment'] = introduce_comment
        context['sidebar_user_extra_info'] = user_extra_info
        context['sidebar_user_sns_info_list'] = user_sns_info_list
        context['member_info'] = user_member_info
        context['page_info'] = page_info
        
        return context