from django.shortcuts import get_object_or_404, render
from django.views.generic import View, TemplateView, DetailView
from django.views.generic.detail import SingleObjectMixin

from fromleaf_common.models.user import User, ExtraUserInfo, MemberInfo 
from fromleaf_common.models.comment import SimpleComment
from fromleaf_common.models.page import PageData
from fromleaf_aboutme.models import AboutMePage

def get_current_user_info(user_member_info):
    return get_object_or_404(User, pk=user_member_info.user.id)
    
def get_current_user_extra_info(user_member_info):
    user_info= get_current_user_info(user_member_info)
    return get_object_or_404(ExtraUserInfo, user=user_info)
    
def get_current_page_info(view_class, user_member_info):
    user_info= get_current_user_info(user_member_info)
    current_page_data = get_object_or_404(PageData, user=user_info)
    current_page_info = None
    
    if view_class.__class__.__name__ is 'AboutMeView':
        current_page_info = get_object_or_404(AboutMePage, page_data=current_page_data)
        
    else:
        pass
    
    return current_page_info


def get_simple_comment_list(view_class, user_member_info):
    user_info= get_current_user_info(user_member_info)
    current_page_data = get_object_or_404(PageData, user=user_info)
    simple_comment_list = None
    
    if view_class.__class__.__name__ is 'AboutMeView':
        current_aboutme_comment = AboutMePage.objects.filter(page_data=current_page_data)
        simple_comment_list = SimpleComment.objects.filter(aboutme_comment=current_aboutme_comment)
        
    else:
        pass
    
    return simple_comment_list


class AboutMeView(TemplateView):
    
    template_name = 'fromleaf_aboutme/aboutme.html'
    
    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data(**kwargs)
        
        site_user_id = 1
        user_email = 'fromleaf@gmail.com'

        user_member_info = get_object_or_404(MemberInfo, email=user_email)
        
        site_user_info = get_current_user_info(user_member_info)
        site_user_extra_info = get_current_user_extra_info(user_member_info)
        page_info = get_current_page_info(self, user_member_info)
        introduce_comment_list = get_simple_comment_list(self, user_member_info)
        
        context['page_info'] = page_info
        context['site_user_info'] = site_user_info
        context['site_user_extra_info'] = site_user_extra_info
        context['simple_comment_list'] = introduce_comment_list
        return context
    
        