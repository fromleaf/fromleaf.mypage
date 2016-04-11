from __future__ import unicode_literals
from django.db import models

from fromleaf_common.models.page import PageContainer
                
class OpeningPage(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(OpeningPage, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.page_name 
    
    page_name = 'OpeningPage'
    page_describe = 'this page is Opening page.'    
    page_container = models.OneToOneField(
                              PageContainer,
                              on_delete=models.CASCADE,
                              )
    
    created_at = models.DateTimeField(auto_now_add=True)