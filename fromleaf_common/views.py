import logging

from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from fromleaf_common.utils import database as db

# TEMP_DATA: 나중에 지워야 함.
USER_EMAIL = 'fromleaf@gmail.com'

class TemplateCommonView(TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super(TemplateCommonView, self).get_context_data(**kwargs)
        user_member_info = db.get_current_member_info(USER_EMAIL)
        user_info = db.get_current_user_info(user_member_info)
        user_extra_info = db.get_current_user_extra_info(user_member_info)
        user_sns_info = db.get_current_user_sns_info(user_member_info)
        # FIXME: 이건 계속 쓰일지 모르겠지만 TEST용으로 사용하는 겁니다.
        comment_list = db.get_comment_list_for_sidebar(user_member_info)

        context['meta_user_info'] = user_info
        context['sidebar_user_info'] = user_info
        context['sidebar_user_introduce_comment'] = comment_list[0]
        context['sidebar_user_extra_info'] = user_extra_info
        context['sidebar_user_sns_info'] = user_sns_info
        context['latest_article_list'] = comment_list[:2]
        context['footer_user_info'] = user_member_info
        
        return context