from django.test import TestCase
from django.conf import settings

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_common.models.comment import SimpleComment
from fromleaf_aboutme.models import AboutMePage

class AboutMePageTestCase(TestCase):
    
    def insert_simple_comment(self, **kwargs):
        simple_comment = SimpleComment.objects.create(**kwargs)
        simple_comment.save()
    
    def insert_aboutme_page_info(self, **kwargs):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_aboutme_page = AboutMePage.objects.create(
                                            page_container=PageContainer.objects.get(member_info=current_member_info)
                                        )
        current_aboutme_page.save()
       
    def insert_simple_comment_data(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_page_container = PageContainer.objects.get(member_info=current_member_info)
        current_aboutme_page = AboutMePage.objects.get(page_container=current_page_container)                                     
         
        self.insert_simple_comment(
                                title='안녕하세요. 간단한 제 소개글입니다.',
                                comment='안녕하세요. 지금 Python을 공부하고 있으며, 이 언어를 이용한 Django Framework를 이용해 웹 개발을 공부하고 있습니다. '
                                + '3년 정도 C를 이용한 임베디드 소프트웨어 개발에 참여했으며, 그 전에는 짧지만 Java를 기반으로한 웹 개발에도 참여했습니다.'
                                + '개발 외에는 책 읽기와 운동 하는 것을 좋아합니다. 책을 읽는 동안은 잠시 조용할 수 있어서 좋아하고, '
                                + '운동은 땀 흘린 뒤의 상쾌함을 좋아합니다.',
                                aboutme_page=current_aboutme_page
                                )
        
    def insert_aboutme_page(self):
        self.insert_aboutme_page_info()
        self.insert_simple_comment_data()