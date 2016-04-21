from django.test import TestCase
from django.conf import settings

from fromleaf_common.models.user import ExtraUserInfo, UserSNSInfo, MemberInfo
from fromleaf_common.models.page import PageContainer
from fromleaf_career.models import CareerPage, Company, Project



class CareerPageTestCase(TestCase):
    
    
    def insert_career_page_info(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_career_page = CareerPage.objects.create(
                                                page_container=PageContainer.objects.get(member_info=current_member_info)
                                            )
        current_career_page.save()


    def insert_company(self, current_name, current_simple_desc,
                       current_started_date, current_finished_date, current_desc,
                       current_company_image, current_career_page):
        current_company = Company.objects.create(
                                            name=current_name,
                                            simple_description=current_simple_desc,
                                            started_date=current_started_date,
                                            finished_date=current_finished_date,
                                            description=current_desc,
                                            company_image=current_company_image,
                                            career_page=current_career_page
                                        )
        current_company.save()
        
    def insert_company_info(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_career_page = CareerPage.objects.get(
                                                page_container=PageContainer.objects.get(member_info=current_member_info)
                                            )
        alticast = self.insert_company(
                                        'Alticast',
                                        'IPTV 수신용 STB의 보안모듈인 CAS모듈을 H/E Server로부터 안전하게 내려받고, 안전하게 수행될 수 있도록 하는 iCAS모듈 및 SVM의 개발 및 유지보수 업무를 맡았습니다.',
                                        '2013-03-01',
                                        '2015-09-30',
                                        'Startup 회사로 시작해 중견기업으로 성장한 회사였습니다. 중견기업이 됐음에도 Startup 회사의 문화를 계속 유지하고 있던 회사였습니다. '
                                        + '그러한 문화가 장단점을 가지고 있다는 것을 알고 있는데, 제가 속해있던 팀은 단점보다 장점이 많았던 팀이었습니다.'
                                        + '좋은 멘토 분과 좋은 팀원분들을 만나, 개발자로써 좋은 조언을 많이 들을 수 있었던 회사였습니다. 기술적인 부분뿐만 아니라 다른 팀간의 협업, '
                                        + '다른 회사 간의 협업, 이슈 대응, 문서화 등 개발뿐만 아니라 그 외적으로 필요한 전체적인 개발 과정을 배웠습니다. 또한 한 사람의 사회인으로써 '
                                        + '갖춰야 하는 인성을 배울 수 있었던 시간이었습니다. 이러한 장점에도 회사를 그만둔 것은 계속 이곳에 있으면 편안함에 빠져버릴 것 같은 '
                                        + '두려움 비슷한 감정을 느꼈습니다. 그래서 마지막 프로젝트를 마무리하고 회사를 그만두게 되었습니다.',
                                        'photos/company/alticast_logo.png',
                                        current_career_page 
                                        )
        acriil = self.insert_company(
                                      'Acriil',
                                      '한글 및 영어 문장에서 감성을 분석하는 엔진 유지보수 및 감성 엔진을 이용한 Web 서비스 개발 및 유지보수 업무에 참여했습니다.',
                                      '2012-05-01',
                                      '2012-10-30',
                                      '인턴 경험과 면접 당시 “잘 모르는 부분입니다.”라고 말할 수 있는 용기(?) 덕분에 팀장님께서 좋게 봐주셔서 입사할 수 있었습니다. '
                                      + '사용자의 문장에서 패턴과 단어가 담고 있는 감정을 분석한 결과 값을 이용해 서비스를 제공하려 했던 Startup회사였습니다.'
                                      + 'Startup이 가지고 있는 장점을 많이 가지고 있던 회사였습니다. 수평적 조직, 유연함, 언제든 자신의 아이디어를 얘기하고 '
                                      + '다른 분들의 의견을 듣고 실제 서비스에 반영할 수 있는 그런 분위기였습니다. 이곳에서 저는 전체적인 개발 라이프 사이클을 배웠습니다. '
                                      + '신규 서비스를 기획하고, 설계하고, 구현하고, 테스트하고, 릴리즈 하는 과정 전체를 배웠습니다. 또한 자신의 의견을 표현하는 법, '
                                      + '실제 수업 시간과 책을 통해 배운 것들을 해볼 수 있었던 좋은 기회였습니다.',
                                      'photos/company/acriil_logo.png',
                                      current_career_page
                                      )
        ibm = self.insert_company(
                                   '한국IBM',
                                   '대학교와 한국IBM과의 연계로 약 5개월간 Internship에 참여했습니다. ' 
                                   + '맡았던 업무는 한국 IBM이 관리하고 있던 아모레퍼시픽의 상품 관리 및 인사 관리 사이트 유지보수 업무를 했습니다.',
                                   '2011-09-01',
                                   '2012-02-28',
                                   '회사라는 곳을 처음 경험했습니다. 회사에서의 모든 것들이 처음 경험해보는 것이었습니다. 출근, 퇴근, 회식, Workshop 등등. '
                                   '그리고 대학교 4년이라는 시간 동안 배운 것들(개발, 개발과정, 문서화 등)을 직접 해볼 수 있었습니다. 그렇게 대학생활 중 가장 점수가 '
                                   + '좋았던 2등을 하는 성적을 받고, 입사 제안도 받았습니다. 그러나 조금 더 유연한 곳에서 개발 경험을 쌓고 싶어서 취업 준비생이 되었습니다.',
                                   'photos/company/ibm_logo.png',
                                   current_career_page
                                   )
    
    def insert_project(self, **kwargs):
        current_project = Project.objects.create(title=kwargs['title'],
                                                  simple_description=kwargs['simple_description'],
                                                  duty_description=kwargs['duty_description'],
                                                  started_date=kwargs['started_date'],
                                                  finished_date=kwargs['finished_date'],
                                                  language=kwargs['language'],
                                                  system=kwargs['system'],
                                                  framework=kwargs['framework'],
                                                  database=kwargs['database'],
                                                  thumnail_image=kwargs['thumnail_image'],
                                                  architecture_image=kwargs['architecture_image'],
                                                  architecture_describe=kwargs['architecture_describe'],
                                                  company=kwargs['company'])                                               
        current_project.save()

        
    def insert_project_info(self):
        current_member_info = MemberInfo.objects.get(email=settings.USER_EMAIL)
        current_career_page = CareerPage.objects.get(
                                                page_container=PageContainer.objects.get(member_info=current_member_info)
                                            )
        current_company_list = Company.objects.filter(career_page=current_career_page)
        alticast_company = current_company_list.get(name='Alticast')
        acriil_company = current_company_list.get(name='Acriil')
        ibm_company = current_company_list.get(name='한국IBM')
        
        alticast_project_01 = self.insert_project(
                                                  title='2013년도 KT 고도화 프로젝트 참여',
                                                  simple_description='기존 CAS Update 방식은 H/E Server에 저장된 CAS 보안 모듈을 Server에서 직접 내려주는 형태였는데, '
                                                  + 'CAS별 버전을 STB 에서 확인하여 H/E Server에 상향 접속하여 Update할 수 있는 시스템 설계 및 개발 참여',
                                                  duty_description='유지보수 업무 진행',
                                                  started_date='2013-04-01',
                                                  finished_date=None,
                                                  language='C',
                                                  system='Ubuntu 12.04',
                                                  framework=None,
                                                  database=None,
                                                  thumnail_image='photos/project/alticast_00.jpeg',
                                                  architecture_image='photos/architecture/alticast_project_00.png',
                                                  architecture_describe='STB 부팅 중에 STB내 보안 모듈 버전을 확인하여, 최신 버전이 아닌 경우 H/E Server에 접속하여 새로운 보안 모듈을 다운로드 받습니다.',
                                                  company=alticast_company                                   
                                                )
        alticast_project_01 = self.insert_project(
                                                  title='KT 올인원 PC(일체형 IPTV PC) -  iCAS 모듈 포팅',
                                                  simple_description='Linux 환경에서 실행되던 iCAS 모듈을 Windows 64bit환경에서 실행될 수 있도록 바이너리 형태로 릴리즈 되던 '
                                                  + '라이브러리를 DLL형태로 릴리즈 될 수 있도록 포팅',
                                                  duty_description='기존 Linux환경에서 빌드 시에 사용하고 있던 오픈 소스 라이브러리를 '
                                                  + 'Windows 환경에서 사용할 수 있도록 빌드 후 Windows환경에서 수행되는 iCAS에 적용',
                                                  started_date='2014-12-01',
                                                  finished_date=None,
                                                  language='C - Visual Studio 2013',
                                                  system='Windows 7 (64bit)',
                                                  framework=None,
                                                  database=None,
                                                  thumnail_image='photos/project/alticast_01.jpeg',
                                                  architecture_image=None,
                                                  architecture_describe=None,
                                                  company=alticast_company
                                                )
        alticast_project_02 = self.insert_project(
                                                   title='iCAS모듈 유지보수',
                                                   simple_description='KT에서 운영 중에 발생한 이슈 대응 및 iCAS 모듈 관련 KT내 인증 테스트 진행 및 한국정보통신기술협회(TTA)에서 진행되는 인증절차 진행',
                                                   duty_description='유지보수 업무 진행',
                                                   started_date='2013-03-30',
                                                   finished_date=None,
                                                   language='C',
                                                   system='Ubuntu 12.04',
                                                   framework=None,
                                                   database=None,
                                                   thumnail_image='photos/project/alticast_02.jpeg',
                                                   architecture_image=None,
                                                   architecture_describe=None,
                                                   company=alticast_company
                                                )
        
        acriil_project_01 = self.insert_project(
                                                   title='HeartSay',
                                                   simple_description='대니얼 골만의 E.I 측정 기준 5가지(자기 감정 인식 능력, 자기 감정 통제 능력, 자아 동기 부여 능력, 타인 감정 인식 및 이입 능력, 커뮤니케이션 활성화 정도)를 기반으로 한 캐릭터 분석 엔진 개발',
                                                   duty_description='Facebook 사용자의 Feed를 Facebook API로 가져와, 구문 분석기를 이용, 문장을 나누고 그 Data를 기반으로 5가지 영역에 대입, 그 결과 값을 기반으로 캐릭터 분석하는 App 개발',
                                                   started_date='2012-05-01',
                                                   finished_date=None,
                                                   language='Java',
                                                   system=None,
                                                   framework='Spring',
                                                   database='MySQL',
                                                   thumnail_image='photos/project/acriil_00.jpeg',
                                                   architecture_image='photos/architecture/acriil_project_00.png',
                                                   architecture_describe='Facebook 사용자의 동의하에 Feed를 가져와 감성 분석을 진행 한 후, 결과값을 이용해 각각의 영역별 감성 분석 결과를 보여줍니다.',
                                                   company=acriil_company
                                                )
        acriil_project_02 = self.insert_project(
                                                   title='LLAMP (시연용 Prototype 개발)',
                                                   simple_description='감성 검색 엔진을 기반으로 Facebook 사용자의 Feed의 감성을 분석. 그 Data를 기반하여 사용자의 패턴을 분석한다. 분석 결과와 자체적으로 분석한 영화 패턴을 매칭하여 사용자에게 영화를 추천해주는 프로그램 개발',
                                                   duty_description=None,
                                                   started_date='2012-06-01',
                                                   finished_date=None,
                                                   language='Java',
                                                   system=None,
                                                   framework='JSP & Servlet',
                                                   database='MySQL',
                                                   thumnail_image='photos/project/acriil_01.jpeg',
                                                   architecture_image='photos/architecture/acriil_project_00.png',
                                                   architecture_describe='Facebook 사용자의 동의하에 Feed를 가져와 감성 분석을 진행 한 후, 결과값을 이용해 사용자의 감성과 유사한 영화를 추천해줍니다.',
                                                   company=acriil_company
                                                )
        acriil_project_03 = self.insert_project(
                                                   title='Complex Affect',
                                                   simple_description='HeartSay 프로젝트의 알고리즘을 기반으로 영화 속 캐릭터의 대사를 분석하여 나온 결과를 기반으로 캐릭터를 분석하는 엔진 개발',
                                                   duty_description=None,
                                                   started_date='2012-09-01',
                                                   finished_date=None,
                                                   language='Java',
                                                   system=None,
                                                   framework='JSP & Servlet',
                                                   database='MySQL',
                                                   thumnail_image='photos/project/acriil_02.jpeg',
                                                   architecture_image=None,
                                                   architecture_describe=None,
                                                   company=acriil_company
                                                )
        
        ibm_project_01 = self.insert_project(
                                               title='상품 및 인사 관리 프로젝트',
                                               simple_description='아모레퍼시픽의 상품 및 인사 관리',
                                               duty_description='고객사의 요구사항에 따라 기능 추가 및 유지보수하는 업무',
                                               started_date='2012-09-01',
                                               finished_date=None,
                                               language='Java',
                                               system=None,
                                               framework='Struts',
                                               database='Oracle DB',
                                               thumnail_image='photos/project/ibm_01.jpeg',
                                               architecture_image='photos/architecture/ibm_project_00.png',
                                               architecture_describe='고객사의 요구사항을 분석, 구현하는 작업입니다.',
                                               company=ibm_company
                                            )
            
    def insert_career_page(self):
        self.insert_career_page_info()
        self.insert_company_info()
        self.insert_project_info()
        
