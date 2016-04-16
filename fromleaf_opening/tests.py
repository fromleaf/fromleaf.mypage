from django.test import TestCase

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_common.models.comment import SimpleComment
from fromleaf_opening.models import OpeningPage

USER_EMAIL = 'fromleaf@gmail.com'

class OpeningPageTestCase(TestCase):
    def insert_opening_page_info(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_opening_page = OpeningPage.objects.create(
                                                page_container=PageContainer.objects.get(member_info=test_member_info)
                                            )
        test_opening_page_comment_01 = SimpleComment.objects.create(
                                    title='제 Portfolio 를 위한 사이트입니다. 궁금하신 사항은 제 메일주소로 연락주세요.',
                                    comment= 'title:Development Environment,'
                                        + 'main_describe_1:이 사이트 개발환경 입니다.,'
                                        + 'language:Python 3.4.1,'
                                        + 'framework:Django 1.9.5,'
                                        + 'database:SQLite,'
                                        + 'cloud_server:Azure - Web Apps(PTVS),'
                                        + 'ui_design: Bootstrap,'
                                        + 'describe_1:이 사이트의 코드는,'
                                        + 'describe_2:공개되어 있습니다.,'
                                        + 'github_address:https://github.com/fromleaf/fromleaf.mypage',
                                    opening_page=test_opening_page
                                )
        
        test_opening_page.save()
        test_opening_page_comment_01.save()