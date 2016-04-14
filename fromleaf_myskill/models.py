from django.db import models

from fromleaf_common.models.page import PageContainer
                
class MySkillPage(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(MySkillPage, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.page_name 
    
    page_name = 'MySkillPage'
    page_describe = 'This page is Introduce My Skill Page.'    
    page_container = models.OneToOneField(
                              PageContainer,
                              on_delete=models.CASCADE,
                              )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class SkillSet(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(SkillSet, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
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