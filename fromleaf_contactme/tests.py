from django.test import TestCase
from django.conf import settings

from fromleaf_common.models.user import MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_contactme.models import ContactMePage

class ContactMePageTestCase(TestCase):
    
    def insert_contactme_page_info(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_page_container = PageContainer.objects.get(member_info=current_member_info)
        current_contactme_page = ContactMePage.objects.create(
                                                page_container=current_page_container
                                            )
        current_contactme_page.save()
        
    def insert_contactme_page(self):
        self.insert_contactme_page_info()