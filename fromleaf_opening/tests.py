from django.test import TestCase
from django.conf import settings

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_common.models.comment import SimpleComment
from fromleaf_opening.models import OpeningPage


class OpeningPageTestCase(TestCase):
    
    def insert_opening_comment(self, **kwargs):
        opening_page_comment = SimpleComment.objects.create(**kwargs)
        opening_page_comment.save()
    
    def insert_opening_page_info(self):
        _member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        opening_page = OpeningPage.objects.create(
                                                page_container=PageContainer.objects.get(member_info=_member_info)
                                            )
        opening_page.save()
    
    def insert_opening_comment_data(self):
<<<<<<< HEAD
        _member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        _page_container = PageContainer.objects.get(member_info=_member_info)
        _opening_page = OpeningPage.objects.get(page_container=_page_container)
        self.insert_opening_comment(
                                   title='저를 소개하기 위한 사이트입니다. 궁금하신 사항은 제 메일주소로 연락주세요.',
                                   comment='title:Development Environment,'
                                    + 'main_describe_1:이 사이트 개발환경 입니다.,'
                                    + 'language:Python 3.4.1,'
                                    + 'framework:Django 1.9.5,'
                                    + 'database:SQLite,'
                                    + 'cloud_server:Azure - Web Apps(PTVS),'
                                    + 'ui_design: Bootstrap,'
                                    + 'describe_1:이 사이트의 코드는,'
                                    + 'describe_2:공개되어 있습니다.,'
                                    + 'github_address:https://github.com/fromleaf/fromleaf.mypage',
                                    opening_page=_opening_page
                                )
=======
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_page_container = PageContainer.objects.get(member_info=current_member_info)
        current_opening_page = OpeningPage.objects.get(page_container=current_page_container)
        current_opening_page_comment = self.insert_opening_comment(
                                                                   title='저를 소개하기 위한 사이트입니다. 궁금하신 사항은 제 메일주소로 연락주세요.',
                                                                   comment='title:Development Environment,'
                                                                    + 'main_describe_1:이 사이트 개발환경 입니다.,'
                                                                    + 'language:Python 3.4.1,'
                                                                    + 'framework:Django 1.9.5,'
                                                                    + 'database:SQLite,'
                                                                    + 'cloud_server:AWS - Beanstalk,'
                                                                    + 'ui_design: Bootstrap,'
                                                                    + 'describe_1:이 사이트의 코드는,'
                                                                    + 'describe_2:공개되어 있습니다.,'
                                                                    + 'github_address:https://github.com/fromleaf/fromleaf.mypage',
                                                                    opening_page=current_opening_page
                                                                    )
>>>>>>> 4757748303d2c9ea453e8f68550a8158094bbdc5
        
    def insert_opening_page(self):
        self.insert_opening_page_info()
        self.insert_opening_comment_data()
        
