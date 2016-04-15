from django.test import TestCase

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_common.models.comment import SimpleComment
from fromleaf_aboutme.models import AboutMePage

USER_EMAIL = 'fromleaf@gmail.com'

class AboutMePageTestCase(TestCase):
        
    def insert_aboutme_page_info(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_aboutme_page = AboutMePage.objects.create(
                                                page_container=PageContainer.objects.get(member_info=test_member_info)
                                            )                                      
         
        test_simple_comment_0 = SimpleComment.objects.create(
                                    title='좋아하는 걸 하려합니다.',
                                    comment= '안녕하세요. 지금 Python을 공부하고 있으며, 이 언어를 이용한 Django Framework를 이용해 웹 개발을 공부하고 있습니다. '
                                            + '3년 정도 C를 이용한 임베디드 소프트웨어 개발에 참여했으며, 그 전에는 짧지만 Java를 기반으로한 웹 개발에도 참여했습니다.'
                                            + '개발 외에는 책 읽기와 운동 하는 것을 좋아합니다. 책을 읽는 동안은 잠시 조용할 수 있어서 좋아하고, '
                                            + '운동은 땀 흘린 뒤의 상쾌함을 좋아합니다.',
                                    aboutme_page=test_aboutme_page
                                )
        test_simple_comment_1 = SimpleComment.objects.create(
                                    title='test_simple_comment_1',
                                    comment= 'Today is Eddie’s eighth birthday, but he is not happy. '
                                        + 'He had hoped to show his truck to his friends at a birthday party. '
                                        + 'Instead, his family have to go someplace and get dressed up. '
                                        + 'Even he is wearing Joe’s old shoes. They go to attend the funeral. '
                                        + 'Eddie watches a man shovel dirt into a hole. The story is back again, '
                                        + 'Eddie and the Blue man are in the Ruby Pier in the heaven. ',
                                    aboutme_page=test_aboutme_page
                                )
        
        test_simple_comment_2 = SimpleComment.objects.create(
                                    title='test_simple_comment_2',
                                    comment= 'Today is Eddie’s eighth birthday, but he is not happy. '
                                        + 'He had hoped to show his truck to his friends at a birthday party. '
                                        + 'Instead, his family have to go someplace and get dressed up. '
                                        + 'Even he is wearing Joe’s old shoes. They go to attend the funeral. '
                                        + 'Eddie watches a man shovel dirt into a hole. The story is back again, '
                                        + 'Eddie and the Blue man are in the Ruby Pier in the heaven. ',
                                    aboutme_page=test_aboutme_page
                                )                                         
        
        test_aboutme_page.save()
        test_simple_comment_0.save()
        test_simple_comment_1.save()
        test_simple_comment_2.save()
    
    
    # 이게 되면 좋을텐데 aboutme_page=test_aboutme_page에서 
    # IndexError: list assignment index out of range 이 에러 메시지가 나온다.
    def insert_introduce_simple_comment(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_page_container = PageContainer.objects.get(member_info=test_member_info)
        test_aboutme_page = AboutMePage.objects.get(page_container=test_page_container)
        test_simple_comment_list = []
        
        for i in range(0, 4):
            test_simple_comment_list[i] = SimpleComment.objects.create(
                                        title='simple_comment_' + str(i),
                                        comment='Today is Eddie’s eighth birthday, but he is not happy. '
                                            + 'He had hoped to show his truck to his friends at a birthday party. '
                                            + 'Instead, his family have to go someplace and get dressed up. '
                                            + 'Even he is wearing Joe’s old shoes. They go to attend the funeral. '
                                            + 'Eddie watches a man shovel dirt into a hole. The story is back again, '
                                            + 'Eddie and the Blue man are in the Ruby Pier in the heaven. '
                                            + 'Eddie got a shock because he didn’t know about the accident. '
                                            + 'However, Eddie thought he paid for his sin because he was in the Blue man’s heaven, '
                                            + 'but The Blue man said that he would teach about there are no random acts to him.',
                                        aboutme_page=test_aboutme_page
                                    )
        for i in range(0, 4):
            test_simple_comment_list[i].save()
        
