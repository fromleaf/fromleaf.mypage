from django.test import TestCase

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_career.models import CareerPage, Company, Project

USER_EMAIL = 'fromleaf@gmail.com'

class CareerPageTestCase(TestCase):
    
    def insert_career_page_info(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_career_page = CareerPage.objects.create(
                                                page_container=PageContainer.objects.get(member_info=test_member_info)
                                            )
        test_career_page.save()
        
    def insert_company_info(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_career_page = CareerPage.objects.get(
                                                page_container=PageContainer.objects.get(member_info=test_member_info)
                                            )
        test_company_01 = Company.objects.create(
                                            name='test_company_01',
                                            simple_description = 'simple test_company_01',
                                            started_date = '2015-01-01',
                                            finished_date = '2015-03-04',
                                            description='This is a test_company_01',
                                            company_image='photos/company/darly.jpeg',
                                            career_page=test_career_page
                                        )
        test_company_02 = Company.objects.create(
                                            name='test_company_02',
                                            simple_description = 'simple test_company_02',
                                            started_date = '2014-01-01',
                                            finished_date = '2014-06-04',
                                            description='This is a test_company_02',
                                            company_image='photos/company/darly.jpeg',
                                            career_page=test_career_page
                                        )
        
        test_company_01.save()
        test_company_02.save()
        
    def insert_project_info(self):
        test_member_info = MemberInfo.objects.get(email=USER_EMAIL)
        test_career_page = CareerPage.objects.get(
                                                page_container=PageContainer.objects.get(member_info=test_member_info)
                                            )
        test_company_list = Company.objects.filter(career_page=test_career_page)
        
        for test_company in test_company_list:
            test_project_01 = Project.objects.create(
                                                    title='test_project_01',
                                                    simple_description = 'test_project_01',
                                                    duty_description = 'do test_project_01',
                                                    started_date = '2015-03-01',
                                                    finished_date = '2015-07-04',
                                                    language='C',
                                                    system='Linux',
                                                    framework='',
                                                    architecture_image='photos/architecture/darly.jpeg',
                                                    architecture_describe='photos/architecture/darly.jpeg',
                                                    company=test_company
                                                )
            test_project_02 = Project.objects.create(
                                                    title='test_project_02',
                                                    simple_description = 'test_project_02',
                                                    duty_description = 'do test_project_02',
                                                    started_date = '2015-01-01',
                                                    finished_date = '2015-03-04',
                                                    language='Java',
                                                    system='Windows',
                                                    framework='Spring',
                                                    architecture_image='photos/architecture/darly.jpeg',
                                                    architecture_describe='photos/architecture/darly.jpeg',
                                                    company=test_company
                                                )
            test_project_03 = Project.objects.create(
                                                    title='test_project_03',
                                                    simple_description = 'test_project_03',
                                                    duty_description = 'do test_project_03',
                                                    started_date = '2013-03-01',
                                                    finished_date = '2014-06-04',
                                                    language='Python',
                                                    system='Ubuntu',
                                                    framework='Django',
                                                    architecture_image='photos/architecture/darly.jpeg',
                                                    architecture_describe='photos/architecture/darly.jpeg',
                                                    company=test_company
                                                )
            test_project_04 = Project.objects.create(
                                                    title='test_project_04',
                                                    simple_description = 'test_project_04',
                                                    duty_description = 'do test_project_04',
                                                    started_date = '2011-02-01',
                                                    finished_date = '2012-08-04',
                                                    language='SQL',
                                                    system='Ubuntu 12.04',
                                                    framework='Django',
                                                    architecture_image='photos/architecture/darly.jpeg',
                                                    architecture_describe='photos/architecture/darly.jpeg',
                                                    company=test_company
                                                )
            test_project_01.save()
            test_project_02.save()
            test_project_03.save()
            test_project_04.save()
            
    def insert_career_page_all(self):
        self.insert_career_page_info()
        self.insert_company_info()
        self.insert_project_info()
        