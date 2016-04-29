from django.test import TestCase
from django.conf import settings

from fromleaf_common.models.user import MemberInfo
from fromleaf_common.models.page import PageContainer

from fromleaf_playing.models import PlayingPage

class PlayingPageTestCase(TestCase):
    
    def insert_playing_page_info(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_playing_page = PlayingPage.objects.create(
                                                page_container=PageContainer.objects.get(member_info=current_member_info)
                                            )
        current_playing_page.save()
        
    def insert_playing_page(self):
        self.insert_playing_page_info()
