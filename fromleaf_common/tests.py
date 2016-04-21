from django.test import TestCase
from django.conf import settings

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, Education, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_common.utils import database as db

class UserTestCase(TestCase):
    
    def set_sns_address(self, sns_name):
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


    def create_sns_info(self, current_sns_name, current_user_id):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL) 
        current_extra_user_info = ExtraUserInfo.objects.get(member_info=current_member_info)
        
        current_sns_address = self.set_sns_address(current_sns_name)
        
        current_sns_info = UserSNSInfo.objects.create(
                                                sns_name=current_sns_name,
                                                sns_address=current_sns_address,
                                                user_id=current_user_id,
                                                extra_user_info=current_extra_user_info
                                            )
        current_sns_info.save()
        
    def insert_education_info(self, current_name, current_kind, current_major, current_score, 
                              current_entranced_date, current_graduate_date, current_extra_user_info):
        current_education = Education.objects.create(
                                                name=current_name,
                                                kind=current_kind,
                                                major=current_major,
                                                score=current_score,
                                                entranced_date=current_entranced_date,
                                                graduated_date=current_graduate_date,
                                                extra_user_info=current_extra_user_info
                                                )
        current_education.save()
    
    
    def insert_member_info(self):
        current_member_info = MemberInfo.objects.create(
                                            email=settings.USER_EMAIL,
                                            password='1234',
                                            grade='OWNER',
                                        )
        current_member_info.save()
     
    def insert_extra_user_info(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL) 
        current_extra_user_info = ExtraUserInfo.objects.create(
                                                    name='Heo Yun',
                                                    birthday='1984-08-06',
                                                    address='경기도 남양주시 와부읍 덕소리 진도아파트 106동 1604',
                                                    phone_number='0315218508',
                                                    cellphone_number='01089481379',
                                                    profile_image='photos/profile/myphoto.jpg',
                                                    blog_address='http://fromleaf.tistory.com',
                                                    member_info=current_member_info,
                                                )
        current_extra_user_info.save()
    
    def insert_user_education_info(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL) 
        current_extra_user_info = ExtraUserInfo.objects.get(member_info=current_member_info)
        self.insert_education_info(
                              '동화고등학교',
                              'HIGH_SCHOOL',
                              None,
                              0.0,
                              None,
                              '2003-02-23',
                              current_extra_user_info
                              )
        self.insert_education_info(
                              '명지대학교',
                              'UNIVERSITY',
                              'Computer Engineering',
                              2.86,
                              '2004-03-02',
                              '2012-02-23',
                              current_extra_user_info
                              )
        
    
    def insert_sns_user_info(self):  
        self.create_sns_info('FACEBOOK', 'fromleaf') 
        self.create_sns_info('GITHUB', 'fromleaf')
        self.create_sns_info('LINKEDIN', 'fromleaf')
        
    def insert_page_container(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL) 
        current_page_container = PageContainer.objects.create(
                                                    member_info=current_member_info,
                                                    title='page_container'
                                                )
        
        current_page_container.save()
        
   
        
        
    def insert_user(self):
        self.insert_member_info()
        self.insert_extra_user_info()
        self.insert_page_container()
        self.insert_user_education_info()
        self.insert_sns_user_info()
        
        
