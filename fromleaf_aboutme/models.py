from __future__ import unicode_literals
from django.db import models

from fromleaf_common.models.page import PageContainer
                
class AboutMePage(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(AboutMePage, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.page_name 
    
    page_name = 'AboutMePage'
    page_describe = 'This page is About Me page.'    
    page_container = models.OneToOneField(
                              PageContainer,
                              on_delete=models.CASCADE,
                              )
    
    created_at = models.DateTimeField(auto_now_add=True)
    