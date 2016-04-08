from django.shortcuts import get_object_or_404, render
from django.views.generic import View, TemplateView, DetailView
from django.views.generic.detail import SingleObjectMixin

from fromleaf_common.models.user import UserInfo, ExtraUserInfo, MemberInfo 
from fromleaf_common.models.comment import SimpleComment
from fromleaf_common.models.page import PageContainer
from fromleaf_aboutme.models import AboutMePage

# TEMP_DATA: 나중에 지워야 함.
USER_EMAIL = 'fromleaf@gmail.com'

def get_current_user_info(user_member_info):
    return get_object_or_404(UserInfo, pk=user_member_info.user_info.id)
    
def get_current_user_extra_info(user_member_info):
    current_user_info= get_current_user_info(user_member_info)
    return get_object_or_404(ExtraUserInfo, user_info=current_user_info)
    
def get_current_page_info(view_class, user_member_info):
    current_user_info= get_current_user_info(user_member_info)
    current_page_container = get_object_or_404(PageContainer, user_info=current_user_info)
    current_page_info = None
    
    if view_class.__class__.__name__ is 'AboutMeView':
        current_page_info = get_object_or_404(AboutMePage, page_container=current_page_container)
        
    else:
        pass
    
    return current_page_info


def get_simple_comment_list(view_class, user_member_info):
    current_user_info= get_current_user_info(user_member_info)
    current_page_container = get_object_or_404(PageContainer, user_info=current_user_info)
    simple_comment_list = None
    
    if view_class.__class__.__name__ is 'AboutMeView':
        current_aboutme_page = AboutMePage.objects.filter(page_container=current_page_container)
        simple_comment_list = SimpleComment.objects.filter(aboutme_page=current_aboutme_page)
        
    else:
        pass
    
    return simple_comment_list


class AboutMeView(TemplateView):
    
    template_name = 'fromleaf_aboutme/aboutme.html'
    
    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data(**kwargs)
        
        user_member_info = get_object_or_404(MemberInfo, email=USER_EMAIL)
        
        site_user_info = get_current_user_info(user_member_info)
        site_user_extra_info = get_current_user_extra_info(user_member_info)
        page_info = get_current_page_info(self, user_member_info)
        introduce_comment_list = get_simple_comment_list(self, user_member_info)
        
        context['page_info'] = page_info
        context['site_user_info'] = site_user_info
        context['site_user_extra_info'] = site_user_extra_info
        context['simple_comment_list'] = introduce_comment_list
        return context
    
        