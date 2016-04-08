from django.test import TestCase

from fromleaf_common.models.user import UserInfo, ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_aboutme.models import AboutMePage
from fromleaf_common.models.comment import SimpleComment


USER_EMAIL = 'fromleaf@gmail.com'

class UserTestCase(TestCase):
    
    def insert_user_info(self):
        test_user_info = UserInfo.objects.create(name='Jeff', birthday='1984-08-06')
        test_member_info = MemberInfo.objects.create(
                                            email=USER_EMAIL,
                                            password='1234',
                                            grade='OWNER',
                                            user_info=test_user_info
                                        )
        test_extra_user_info = ExtraUserInfo.objects.create(
                                                    address='경기도 남양주시 와부읍',
                                                    phone_number='0315555555',
                                                    cellphone_number='01011111234',
                                                    profile_image='photos/profile/darly.jpeg',
                                                    blog_address='http://www.blog.com',
                                                    user_info=test_user_info
                                                )
        test_user_sns_info = UserSNSInfo.objects.create(
                                                    github_id= 'fromleaf',
                                                    github_address= 'http://www.github.com',
                                                    facebook_id= 'fromleaf',
                                                    facebook_address= 'http://www.facebook.com',
                                                    linkedin_id= 'fromleaf',
                                                    linkedin_address= 'http://www.linkedin.com',
                                                    extra_user_info = test_extra_user_info
                                                )
        
        test_user_info.save()
        test_member_info.save()
        test_extra_user_info.save()
        test_user_sns_info.save()
        
    def insert_aboutme_page_info(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_page_container = PageContainer.objects.create(
                                                    user_info=test_member_info.user_info,
                                                    title='page_container'
                                                )
        test_aboutme_page = AboutMePage.objects.create(
                                                page_container=test_page_container
                                            )                                      
         
        test_simple_comment_0 = SimpleComment.objects.create(
                                    title='test_simple_comment_0',
                                    comment= 'Today is Eddie’s eighth birthday, but he is not happy. '
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
        test_simple_comment_1 = SimpleComment.objects.create(
                                    title='test_simple_comment_1',
                                    comment= 'Today is Eddie’s eighth birthday, but he is not happy. '
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
        
        test_simple_comment_2 = SimpleComment.objects.create(
                                    title='test_simple_comment_2',
                                    comment= 'Today is Eddie’s eighth birthday, but he is not happy. '
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
        test_page_container.save()
        test_aboutme_page.save()
        test_simple_comment_0.save()
        test_simple_comment_1.save()
        test_simple_comment_2.save()
    
    
    # 이게 되면 좋을텐데 aboutme_page=test_aboutme_page에서 
    # IndexError: list assignment index out of range 이 에러 메시지가 나온다.
    def insert_introduce_simple_comment(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_page_container = PageContainer.objects.get(user_info=test_member_info.user_info)
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
        
