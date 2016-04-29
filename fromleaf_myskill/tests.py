from django.test import TestCase
from django.conf import settings

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_myskill.models import MySkillPage, SkillSet


class MySkillPageTestCase(TestCase):
    
    def insert_myskill_page_info(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_page_container = PageContainer.objects.get(member_info=current_member_info)
        current_myskill_page = MySkillPage.objects.create(page_container=current_page_container)
        
        current_myskill_page.save()  
    
    def insert_myskill(self, **kwargs):
        current_myskill_set = SkillSet.objects.create(**kwargs)
        current_myskill_set.save()
        
    def insert_development_skill_data(self, current_myskill_page):
        self.insert_myskill(
                            name='C',
                            kind='DEVELOPMENT',
                            level=3,
                            describe='Code를 읽고, 기본적인 개념 및 문법에 맞춰서 프로그램을 개발할 수 있습니다.' 
                             + '기본적인 포인터의 사용법 및 함수형 프로그래밍이 가능하며,'
                             + 'System Call 함수를 이용한 프로그램 작성도 가능합니다.',
                             my_skill_page=current_myskill_page
                             )
        self.insert_myskill(
                            name='Python',
                            kind='DEVELOPMENT',
                             level=2,
                             describe='Code를 읽고, 기본적인 개념 및 문법에 맞춰서 프로그램을 개발할 수 있습니다.' 
                             + '기본 제공되는 라이브러리의 사용법을 읽고, 그 라이브러리를 이용해 프로그램을 만들 수 있습니다.'
                             + '이 사이트를 개발하면서도 이런저런 Python 문법 및 라이브러리를 적용해보면서 작업을 진행했습니다.',
                             my_skill_page=current_myskill_page
                            )
        self.insert_myskill(
                            name='Java',
                            kind='DEVELOPMENT',
                             level=1,
                             describe='Code를 읽고, 기본적인 개념 및 문법에 맞춰서 프로그램을 개발할 수 있습니다.' 
                             + '1년 정도 Java를 이용한 개발에 참여했지만, 시간이 오래되어 지금은 코드를 읽고, '
                             + '프로그램의 흐름 정도만 파악할 수 있는 정도라고 생각됩니다.',
                             my_skill_page=current_myskill_page
                            )
        
    def insert_cooperation_skill_data(self, current_myskill_page):
        self.insert_myskill(
                            name='SVN',
                            kind='COOPERATION',
                             level=3,
                             describe='지금까지 대부분의 프로젝트의 형상관리를 SVN으로 진행하였습니다.',
                             my_skill_page=current_myskill_page
                            )
        self.insert_myskill(
                            name='Git',
                            kind='COOPERATION',
                            level=2,
                             describe='기본적인 명령어의 사용 및 형상관리는 할 수 있는 수준입니다.',
                             my_skill_page=current_myskill_page
                            )
        self.insert_myskill(
                            name='Redmine',
                            kind='COOPERATION',
                             level=3,
                             describe='Redmine에서 제공하는 기본 기능을 이용해서 이슈를 정리하고, 남길 수 있습니다.'
                             + '지난 회사에서 이 툴을 이용해 지속적으로 이슈 트랙킹을 하였습니다.',
                             my_skill_page=current_myskill_page
                            )
        
        
    def insert_os_skill_data(self, current_myskill_page):
        self.insert_myskill(
                            name='Ubuntu',
                            kind='OS',
                             level=2,
                             describe='필요한 경우 패키지를 설치하고, 필요한 경우 사용자 환경을 변경하여,'
                             + '제가 원하는 개발 환경을 만들 수 있습니다. 기본적인 명령어를 사용할 줄 알며,'
                             + '간단한 쉘 스크립트도 작성 가능합니다. Ubuntu에서의 개발환경에도 익숙합니다.',
                             my_skill_page=current_myskill_page
                            )
        self.insert_myskill(
                            name='Mac',
                            kind='OS',
                            level=2,
                             describe='현재 사용중인 OS입니다. 개발환경을 꾸리고, Mac에서 개발하고 있습니다.',
                             my_skill_page=current_myskill_page
                            )
        
    def insert_personality_skill_data(self, current_myskill_page): 
        self.insert_myskill(
                            name='Positive',
                            kind='PERSONALITY',
                             level=4,
                             describe='굉장히 긍정적입니다. 왠만한 일(도리에 어긋나지 않는 일)에는 화를 내지 않습니다.'
                             + '제가 이해할 수 있는 한에서 좋은 면을 보려고 합니다.',
                             my_skill_page=current_myskill_page
                            )
        self.insert_myskill(
                            name='Activity',
                            kind='PERSONALITY',
                             level=2,
                             describe='활발합니다. 긍적적인 영향 떄문일수도 있겠지만, 활발한 편이라 생각됩니다.'
                             + '그러나 항상 그렇지는 않습니다.',
                             my_skill_page=current_myskill_page
                            )
        self.insert_myskill(
                            name='Teamwork',
                           kind='PERSONALITY',
                            level=3,
                             describe='함께 설계하고, 부족한 것을 채워주는 개발 과정을 좋아합니다.'
                             + '혼자 개발하는 것보다는 함께 개발해서 완성 후 그 즐거움을 공유하는 것을 더 좋아합니다.',
                            my_skill_page=current_myskill_page
                            )
        self.insert_myskill(
                            name='Leadership',
                            kind='PERSONALITY',
                             level=1,
                             describe='이 부분은 잘 모르겠습니다. 제 개인적인 생각은'
                             + '그렇게 뛰어난 리더는 아니라고 생각됩니다. 아직 그러기에는 부족함을 많이 느낍니다.',
                             my_skill_page=current_myskill_page
                            )
        
    def insert_myskill_data(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_page_container = PageContainer.objects.get(member_info=current_member_info)                                   
        current_myskill_page = MySkillPage.objects.get(page_container=current_page_container)
         
        self.insert_development_skill_data(current_myskill_page)
        self.insert_cooperation_skill_data(current_myskill_page)
        self.insert_os_skill_data(current_myskill_page)
        self.insert_personality_skill_data(current_myskill_page) 


    def insert_myskill_page(self):
        self.insert_myskill_page_info()
        self.insert_myskill_data()
