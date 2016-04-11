from django.test import TestCase

from fromleaf_common.models.user import UserInfo, ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer

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
        
        test_page_container = PageContainer.objects.create(
                                                    user_info=test_member_info.user_info,
                                                    title='page_container'
                                                )
        
        test_user_info.save()
        test_member_info.save()
        test_extra_user_info.save()
        test_user_sns_info.save()
        test_page_container.save()