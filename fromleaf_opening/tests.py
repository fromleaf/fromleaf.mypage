from django.test import TestCase

from fromleaf_common.models.user import UserInfo, ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_common.models.comment import SimpleComment
from fromleaf_opening.models import OpeningPage

USER_EMAIL = 'fromleaf@gmail.com'

class OpeningPageTestCase(TestCase):
    def insert_opening_page_info(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_opening_page = OpeningPage.objects.create(
                                                page_container=PageContainer.objects.get(user_info=test_member_info.user_info)
                                            )
        test_opening_page_comment_01 = SimpleComment.objects.create(
                                    title='test_opening_page_comment_01',
                                    comment= 'Today is Eddie’s eighth birthday, but he is not happy. '
                                        + 'He had hoped to show his truck to his friends at a birthday party. '
                                        + 'Instead, his family have to go someplace and get dressed up. '
                                        + 'Even he is wearing Joe’s old shoes. They go to attend the funeral. '
                                        + 'Eddie watches a man shovel dirt into a hole. The story is back again, '
                                        + 'Eddie and the Blue man are in the Ruby Pier in the heaven. '
                                        + 'Eddie got a shock because he didn’t know about the accident. '
                                        + 'However, Eddie thought he paid for his sin because he was in the Blue man’s heaven, '
                                        + 'but The Blue man said that he would teach about there are no random acts to him.',
                                    opening_page=test_opening_page
                                )
        
        test_opening_page.save()
        test_opening_page_comment_01.save()