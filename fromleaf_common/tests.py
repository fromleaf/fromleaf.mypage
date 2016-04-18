from django.test import TestCase

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_common.utils import database as db

USER_EMAIL = 'fromleaf@gmail.com'

def set_sns_address(sns_name):
    FACEBOOK_ADDRESS = 'http://www.facebook.com/'
    GITHUB_ADDRESS = 'http://www.github.com/'
    LINKEDIN_ADDRESS = 'http://www.linkedin.com/in/'
    sns_address = ''
    
    if sns_name is 'FACEBOOK':
        sns_address = FACEBOOK_ADDRESS
    elif sns_name is 'GITHUB':
        sns_address = GITHUB_ADDRESS
    elif sns_name is 'LINKEDIN':
        sns_address = LINKEDIN_ADDRESS
        
    return sns_address


def create_sns_info(current_sns_name, current_user_id):
    test_member_info = MemberInfo.objects.get(email=USER_EMAIL) 
    test_extra_user_info = ExtraUserInfo.objects.get(member_info=test_member_info)
    
    current_sns_address = set_sns_address(current_sns_name)
    
    test_sns_info = UserSNSInfo.objects.create(
                                            sns_name = current_sns_name,
                                            sns_address = current_sns_address,
                                            user_id = current_user_id,
                                            extra_user_info = test_extra_user_info
                                        )
    test_sns_info.save()

class UserTestCase(TestCase):

    def insert_member_info(self):
        test_member_info = MemberInfo.objects.create(
                                            email=USER_EMAIL,
                                            password='1234',
                                            grade='OWNER',
                                        )
        test_member_info.save()
     
    def insert_extra_user_info(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL) 
        test_extra_user_info = ExtraUserInfo.objects.create(
                                                    name='Jeff',
                                                    birthday='1984-08-06',
                                                    address='경기도 남양주시 와부읍',
                                                    phone_number='0315555555',
                                                    cellphone_number='01011111234',
                                                    profile_image='photos/profile/darly.jpeg',
                                                    blog_address='http://www.blog.com',
                                                    member_info=test_member_info,
                                                )
        test_extra_user_info.save()
        
    def insert_page_container(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL) 
        test_page_container = PageContainer.objects.create(
                                                    member_info=test_member_info,
                                                    title='page_container'
                                                )
        
        test_page_container.save()
        
    def insert_sns_user_info(self):  
        test_sns_info_0 = create_sns_info('FACEBOOK', 'fromleaf') 
        test_sns_info_1 = create_sns_info('GITHUB', 'fromleaf')
        test_sns_info_2 = create_sns_info('LINKEDIN', 'fromleaf')
        
        
    def insert_user_info(self):
        self.insert_member_info()
        self.insert_extra_user_info()
        self.insert_page_container()
        self.insert_sns_user_info()
        