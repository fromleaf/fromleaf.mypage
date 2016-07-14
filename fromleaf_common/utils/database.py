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
    
def get_current_page_info(view_class, current_member_info):
    """
        - description: 현재 화면에 보여지는 페이지의 정보를 가져온다.
        - get:
            * view_class - 현재 사용되는 view class
            * current_memeber_info: 현재 page사용자 정보
        - return: current_page_info
            * name: 현재 page 이름
            * description: 현재 page 정보
            * created_at: 현재 page database에 생성한 날짜
    """
    current_page_container = get_object_or_404(PageContainer, member_info=current_member_info)
    current_page_info = None

    if view_class.__class__.__name__ is 'AboutMeView':
        current_page_info = get_object_or_404(
            AboutMePage, page_container=current_page_container)
    elif view_class.__class__.__name__ is 'OpeningView':
        current_page_info = get_object_or_404(
            OpeningPage, page_container=current_page_container)
    elif view_class.__class__.__name__ is 'MySkillView':
        current_page_info = get_object_or_404(
            MySkillPage, page_container=current_page_container)
    elif view_class.__class__.__name__ in ['CareerView', 'CompanyDetailView']:
        current_page_info = get_object_or_404(
            CareerPage, page_container=current_page_container)
    elif view_class.__class__.__name__ is 'PlayingView':
        current_page_info = get_object_or_404(
            PlayingPage, page_container=current_page_container)
    elif view_class.__class__.__name__ in ['DarlyMainView',
                                           'DarlyPhotoView']:
        current_page_info = get_object_or_404(
            PlayingPage, page_container=current_page_container)
    elif view_class.__class__.__name__ in ['OurHockeyMainView',
                                           'MemberListView',
                                           'GameScheduleListView',
                                           'SelectTodayAttendListView',
                                           'SelectedTodayAttendListView',
                                           'TodayAttendedMemberListView']:
        current_page_info = get_object_or_404(
            PlayingPage, page_container=current_page_container)
    elif view_class.__class__.__name__ in ['PlaygroundMainView',
                                           'PlaygroundWebCrawlerView']:
        current_page_info = get_object_or_404(
            PlayingPage, page_container=current_page_container)
    elif view_class.__class__.__name__ is 'ContactMeView':
        current_page_info = get_object_or_404(
            ContactMePage, page_container=current_page_container)

    return current_page_info


def get_introduce_comment(current_member_info):
    """
        - description: SimpleComment에 저장된 자신의 소개글 정보를 반환한다.
        - get:
            * current_memeber_info: 현재 page사용자 정보
        - return
            * introduce_comment[0]: 첫번째 comment에 저장된 소개글을 전달한다.
    """
    
    current_page_container = get_object_or_404(
        PageContainer, member_info=current_member_info)
    current_aboutme_page = AboutMePage.objects.filter(
        page_container=current_page_container)
    introduce_comment = SimpleComment.objects.filter(
        aboutme_page=current_aboutme_page)

    # CHECK: 첫번째 값을 전달하는건 아니지 않을까??
    return introduce_comment[0]
      
def get_simple_comment_list(view_class, current_member_info):
    """
        - description: 페이지에 필요한 소개글을 반환한다.
        - get:
            * view_class - 현재 사용되는 view class
            * current_memeber_info: 현재 page사용자 정보
        - return
            * simple_comment_list: Comment 리스트
    """
    current_page_container = get_object_or_404(
        PageContainer, member_info=current_member_info)
    simple_comment_list = None

    if view_class.__class__.__name__ is 'AboutMeView':
        current_aboutme_page = AboutMePage.objects.filter(
            page_container=current_page_container)
        simple_comment_list = SimpleComment.objects.filter(
            aboutme_page=current_aboutme_page)

    elif view_class.__class__.__name__ is 'OpeningView':
        current_opening_page = OpeningPage.objects.filter(
            page_container=current_page_container)
        simple_comment_list = SimpleComment.objects.filter(
            opening_page=current_opening_page)
    else:
        pass
    
    
    if simple_comment_list is None:
        simple_comment_list = [""];
    
    return simple_comment_list


class UserData():
    """
       App 사용자 정보를 가져오기 위한 함수를 모아 놓은 Class
    """
    
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
            self._user_education_info = Education.objects.filter(
                extra_user_info=self._extra_user_info)
        except Education.DoesNotExist:
            raise Http404('Education matches the given query.')

    def set_user_sns_list(self):
        self._user_sns_list = UserSNSInfo.objects.filter(
            extra_user_info=self._extra_user_info)

    def get_member_info(self):
        return self._member_info

    def get_extra_user_info(self):
        return self._extra_user_info

    def get_user_education_info(self):
        return self._user_education_info
     
    def get_user_sns_list(self):
        return self._user_sns_list

class CompanyData():
    """
        Company 정보를 가져오기 위한 함수를 모아 놓은 Class
    """
    def __init__(self, email):
        self._email = email
        self._user_data = UserData(email)
        self._project_list = []
        self.set_company_list()
        self.set_project_all(self._company_list)
        
    def set_company_list(self):
        try:
            self._company_list = Company.objects.filter(
                member_info=self._user_data.get_member_info())
        except Company.DoesNotExist:
            raise Http404('Company matches the given query.')

    def set_project_all(self, company_list):
        if company_list is not None:
            for _company in company_list:
                _project_list = Project.objects.filter(
                    company=_company).order_by('-finished_date')
                self._project_list.append(_project_list)
        else:
            pass

    def get_company_list(self):
        return self._company_list

    def get_project_all(self):
        return self._project_list
    
    def get_project_list_of_company(self, _company):
        try:
            project_list = Project.objects.filter(
                company=_company).order_by('-finished_date')
        except Company.DoesNotExist:
            raise Http404('Company matches the given query.')
        return project_list
