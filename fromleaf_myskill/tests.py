from django.test import TestCase

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_myskill.models import MySkillPage, SkillSet

USER_EMAIL = 'fromleaf@gmail.com'

class MySkillPageTestCase(TestCase):
        
    def insert_myskill_page_info(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_myskill_page = MySkillPage.objects.create(
                                                page_container=PageContainer.objects.get(member_info=test_member_info)
                                            )                                      
         
        test_myskill_set_0 = SkillSet.objects.create(
                                    name='C',
                                    kind='DEVELOPMENT',
                                    level=4,
                                    describe='This is C Language.',
                                    my_skill_page=test_myskill_page
                                )
        
        test_myskill_set_1 = SkillSet.objects.create(
                                    name='Python',
                                    kind='DEVELOPMENT',
                                    level=3,
                                    describe='This is Python Language.',
                                    my_skill_page=test_myskill_page
                                )
        
        test_myskill_set_2 = SkillSet.objects.create(
                                    name='Java',
                                    kind='DEVELOPMENT',
                                    level=2,
                                    describe='This is Java Language.',
                                    my_skill_page=test_myskill_page
                                )
        
        test_myskill_set_3 = SkillSet.objects.create(
                                    name='Windows',
                                    kind='OS',
                                    level=3,
                                    describe='This is Windows.',
                                    my_skill_page=test_myskill_page
                                )
        
        test_myskill_set_4 = SkillSet.objects.create(
                                    name='Leadership',
                                    kind='PERSONALITY',
                                    level=2,
                                    describe='This is Leadership.',
                                    my_skill_page=test_myskill_page
                                )
     
        test_myskill_page.save()
        test_myskill_set_0.save()
        test_myskill_set_1.save()
        test_myskill_set_2.save()
        test_myskill_set_3.save()
        test_myskill_set_4.save()
