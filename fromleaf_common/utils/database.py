import logging

from django.shortcuts import get_object_or_404

from fromleaf_common.models.user import UserInfo, ExtraUserInfo, UserSNSInfo, MemberInfo 
from fromleaf_common.models.comment import SimpleComment
from fromleaf_common.models.page import PageContainer
from fromleaf_opening.models import OpeningPage
from fromleaf_aboutme.models import AboutMePage


logger = logging.getLogger(__name__)

def get_current_member_info(currnet_user_email):
    return get_object_or_404(MemberInfo, email=currnet_user_email)


def get_current_user_info(user_member_info):
    return get_object_or_404(UserInfo, pk=user_member_info.user_info.id)
 
    
def get_current_user_extra_info(user_member_info):
    current_user_info= get_current_user_info(user_member_info)
    return get_object_or_404(ExtraUserInfo, user_info=current_user_info)
 
 
def get_current_user_sns_info(user_member_info):
    current_user_extra_info = get_current_user_extra_info(user_member_info)
    return get_object_or_404(UserSNSInfo, extra_user_info=current_user_extra_info)
     
    
def get_current_page_info(view_class, user_member_info):
    current_user_info= get_current_user_info(user_member_info)
    current_page_container = get_object_or_404(PageContainer, user_info=current_user_info)
    current_page_info = None
    
    if view_class.__class__.__name__ is 'AboutMeView':
        current_page_info = get_object_or_404(AboutMePage, page_container=current_page_container)
    elif view_class.__class__.__name__ is 'OpeningView':
        current_page_info = get_object_or_404(OpeningPage, page_container=current_page_container)
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
    
    elif view_class.__class__.__name__ is 'OpeningView':
        current_opening_page = OpeningPage.objects.filter(page_container=current_page_container)
        simple_comment_list = SimpleComment.objects.filter(opening_page=current_opening_page)
    else:
        pass
    
    
    if simple_comment_list is None:
        simple_comment_list = [""];
    
    return simple_comment_list
