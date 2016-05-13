from django.db import models

from fromleaf_common.models.page import PageContainer

class PlayingPage(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(PlayingPage, self).__init__(*args, **kwargs)

    def __unicode__(self):  # __str__ on Python3
        return self.page_name 
    
    name = 'PlayingPage'
    description = '틈틈히 만들어 보고 있는 Application(?)들 입니다. 소스는 GitHub에 공개되어있습니다.'    
    page_container = models.OneToOneField(
                              PageContainer,
                              on_delete=models.CASCADE,
                              null=True
                              )
    
    created_at = models.DateTimeField(auto_now_add=True)