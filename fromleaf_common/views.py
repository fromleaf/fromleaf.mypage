import logging

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView

from fromleaf_common.utils import database as db
from fromleaf_common.utils.database import UserData

class TemplateCommonView(TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super(TemplateCommonView, self).get_context_data(**kwargs)
        user_data = UserData(settings.USER_EMAIL)
        introduce_comment = db.get_introduce_comment(user_data.get_member_info())
        page_info = db.get_current_page_info(self, user_data.get_member_info())

        context['meta_user_info'] = user_data.get_extra_user_info()
        context['sidebar_user_info'] = user_data.get_extra_user_info()
        context['sidebar_user_introduce_comment'] = introduce_comment
        context['sidebar_user_extra_info'] = user_data.get_extra_user_info()
        context['sidebar_user_sns_info_list'] = user_data.get_user_sns_list()
        context['member_info'] = user_data.get_member_info()
        context['page_info'] = page_info
        
        return context
    
class ListCommonView(ListView):
    
    def get_context_data(self, **kwargs):
        context = super(ListCommonView, self).get_context_data(**kwargs)
        user_data = UserData(settings.USER_EMAIL)
        introduce_comment = db.get_introduce_comment(user_data.get_member_info())
        page_info = db.get_current_page_info(self, user_data.get_member_info())

        context['meta_user_info'] = user_data.get_extra_user_info()
        context['sidebar_user_info'] = user_data.get_extra_user_info()
        context['sidebar_user_introduce_comment'] = introduce_comment
        context['sidebar_user_extra_info'] = user_data.get_extra_user_info()
        context['sidebar_user_sns_info_list'] = user_data.get_user_sns_list()
        context['member_info'] = user_data.get_member_info()
        context['page_info'] = page_info
        
        return context
    
    
class FormCommonView(FormView):
    
    def get_context_data(self, **kwargs):
        context = super(FormCommonView, self).get_context_data(**kwargs)
        user_data = UserData(settings.USER_EMAIL)
        introduce_comment = db.get_introduce_comment(user_data.get_member_info())
        page_info = db.get_current_page_info(self, user_data.get_member_info())

        context['meta_user_info'] = user_data.get_extra_user_info()
        context['sidebar_user_info'] = user_data.get_extra_user_info()
        context['sidebar_user_introduce_comment'] = introduce_comment
        context['sidebar_user_extra_info'] = user_data.get_extra_user_info()
        context['sidebar_user_sns_info_list'] = user_data.get_user_sns_list()
        context['member_info'] = user_data.get_member_info()
        context['page_info'] = page_info
        
        return context
    
    
class DetailCommonView(DetailView):
    
    def get_context_data(self, **kwargs):
        context = super(DetailCommonView, self).get_context_data(**kwargs)
        user_data = UserData(settings.USER_EMAIL)
        introduce_comment = db.get_introduce_comment(user_data.get_member_info())
        page_info = db.get_current_page_info(self, user_data.get_member_info())

        context['meta_user_info'] = user_data.get_extra_user_info()
        context['sidebar_user_info'] = user_data.get_extra_user_info()
        context['sidebar_user_introduce_comment'] = introduce_comment
        context['sidebar_user_extra_info'] = user_data.get_extra_user_info()
        context['sidebar_user_sns_info_list'] = user_data.get_user_sns_list()
        context['member_info'] = user_data.get_member_info()
        context['page_info'] = page_info
        
        return context