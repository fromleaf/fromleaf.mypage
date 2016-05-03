import logging

from django.shortcuts import get_object_or_404

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, Education, MemberInfo 
from fromleaf_common.models.comment import SimpleComment
from fromleaf_common.models.page import PageContainer
from fromleaf_opening.models import OpeningPage
from fromleaf_aboutme.models import AboutMePage
from fromleaf_myskill.models import MySkillPage
from fromleaf_career.models import CareerPage, Company, Project
from fromleaf_playing.models import PlayingPage 
from fromleaf_contactme.models import ContactMePage

logger = logging.getLogger(__name__)

def get_current_member_info(currnet_user_email):
    return get_object_or_404(MemberInfo, email=currnet_user_email)
 
    
def get_current_user_extra_info(current_member_info):
    return get_object_or_404(ExtraUserInfo, member_info=current_member_info)

def get_current_user_education_info(current_member_info):
    current_extra_user_info = get_current_user_extra_info(current_member_info)
    return Education.objects.filter(extra_user_info=current_extra_user_info)
 
def get_current_user_sns_list_info(user_member_info):
    current_user_extra_info = get_current_user_extra_info(user_member_info)
    return UserSNSInfo.objects.filter(extra_user_info=current_user_extra_info)

    
def get_current_page_info(view_class, current_member_info):
    current_page_container = get_object_or_404(PageContainer, member_info=current_member_info)
    current_page_info = None
    
    if view_class.__class__.__name__ is 'AboutMeView':
        current_page_info = get_object_or_404(AboutMePage, page_container=current_page_container)
    elif view_class.__class__.__name__ is 'OpeningView':
        current_page_info = get_object_or_404(OpeningPage, page_container=current_page_container)
    elif view_class.__class__.__name__ is 'MySkillView':
        current_page_info = get_object_or_404(MySkillPage, page_container=current_page_container)
    elif view_class.__class__.__name__ in ['CareerView', 'CompanyDetailView']:
        current_page_info = get_object_or_404(CareerPage, page_container=current_page_container)
    elif view_class.__class__.__name__ is 'PlayingView':
        current_page_info = get_object_or_404(PlayingPage, page_container=current_page_container)
    elif view_class.__class__.__name__ is 'ContactMeView':
        current_page_info = get_object_or_404(ContactMePage, page_container=current_page_container)
    
    return current_page_info


def get_introduce_comment(current_member_info):
    current_page_container = get_object_or_404(PageContainer, member_info=current_member_info)
    current_aboutme_page = AboutMePage.objects.filter(page_container=current_page_container)
    introduce_comment = SimpleComment.objects.filter(aboutme_page=current_aboutme_page)
    
    return introduce_comment[0]
      
def get_simple_comment_list(view_class, current_member_info):
    current_page_container = get_object_or_404(PageContainer, member_info=current_member_info)
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


def get_comment_list_for_sidebar(current_member_info):
    current_page_container = get_object_or_404(PageContainer, member_info=current_member_info)
    
    current_aboutme_page = AboutMePage.objects.filter(page_container=current_page_container)
    comment_list = SimpleComment.objects.filter(aboutme_page=current_aboutme_page)
    
    return comment_list

def get_current_user_company_info(current_member_info):
    current_page_container = get_object_or_404(PageContainer, member_info=current_member_info)
    current_career_page = CareerPage.objects.filter(page_container=current_page_container)
    company_list = Company.objects.filter(career_page=current_career_page)
    
    return company_list

def get_current_project_list(current_company):
    project_list = Project.objects.filter(company=current_company).order_by('-finished_date')
    return project_list


class UserData():
    
    def __init__(self, email):
        self._email = email
        self.set_member_info()
        self.set_extra_user_info()
        self.set_user_education_info()
        self.set_user_sns_list()
    
    def set_member_info(self):
        self._member_info = get_object_or_404(MemberInfo, email=self._email)
        
    def set_extra_user_info(self):
        self._extra_user_info = get_object_or_404(
                                                  ExtraUserInfo, 
                                                  member_info=self._member_info
                                                  ) 
    
    def set_user_education_info(self):
        try:
            self._user_education_info = Education.objects.filter(extra_user_info=self._extra_user_info)
        except Education.DoesNotExist:
            raise Http404('Education matches the given query.')
    
    def set_user_sns_list(self):
        self._user_sns_list = UserSNSInfo.objects.filter(extra_user_info=self._extra_user_info)    
    
    def get_member_info(self):
        return self._member_info
    
    def get_extra_user_info(self):
        return self._extra_user_info
    
    def get_user_education_info(self):
        return self._user_education_info
     
    def get_user_sns_list(self):
        return self._user_sns_list

class CompanyData():
    
    def __init__(self, email):
        self._email = email
        self._user_data = UserData(email)
        self._project_list = []
        self.set_company_list()
        self.set_project_all(self._company_list)
        
    def set_company_list(self):
        try:
            self._company_list = Company.objects.filter(member_info=self._user_data.get_member_info())
        except Company.DoesNotExist:
            raise Http404('Company matches the given query.')
    
    def set_project_all(self, company_list):
        if company_list is not None:
            for _company in company_list:
                _project_list = Project.objects.filter(company=_company).order_by('-finished_date')
                self._project_list.append(_project_list)
        else:
            pass
        
    def get_company_list(self):
        return self._company_list
        
    def get_project_all(self):
        return self._project_list
    
    def get_project_list_of_company(self, _company):
        try:
            project_list = Project.objects.filter(company=_company).order_by('-finished_date')
        except Company.DoesNotExist:
            raise Http404('Company matches the given query.')
        return project_list
