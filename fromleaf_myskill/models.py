from django.db import models

from fromleaf_common.models.page import PageContainer
                
class MySkillPage(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(MySkillPage, self).__init__(*args, **kwargs)
    
    def __unicode__(self):    # __str__ on Python3
        return self.page_name 
    
    name = 'My Skill Page'
    description = '제가 그동안 경험했던 개발 언어 및 협업툴, 그리고 제 성격에 대해 정리해놓았습니다. 굉장히 주관적인 레벨 및 설명입니다. 정확하지 않을 수도 있습니다.'    
    page_container = models.OneToOneField(
                              PageContainer,
                              on_delete=models.CASCADE,
                              null=True
                              )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class SkillSet(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(SkillSet, self).__init__(*args, **kwargs)
    
    def __unicode__(self):    # __str__ on Python3
        return self.name
    
    DEVELOPMENT = 'DEVELOPMENT_TOOL'
    COOPERATION = 'COOPERATION_TOOL'
    OS = 'OS'
    PERSONALITY = 'PERSONALITY'
    ETC = 'ETC'
    
    KIND_CHOICES = (
        (DEVELOPMENT, 'Development'),
        (COOPERATION, 'Cooperation'),
        (OS, 'OS'),
        (PERSONALITY, 'Personality'),
        (ETC, 'etc'),
    )
    
    name = models.CharField(max_length=200)
    kind = models.CharField(
                            max_length=20,
                            choices=KIND_CHOICES,
                            )
    level = models.IntegerField()
    describe = models.TextField(max_length=400)
    my_skill_page = models.ForeignKey(
                                MySkillPage,
                                on_delete=models.CASCADE,
                                null=True
                            )
