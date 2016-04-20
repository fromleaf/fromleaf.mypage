from django.db import models

from fromleaf_common.models.page import PageContainer

class StudyingPage(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(StudyingPage, self).__init__(*args, **kwargs)

    def __unicode__(self):  # __str__ on Python3
        return self.page_name 
    
    name = 'StudyingPage'
    description = 'this page is Studying page.'    
    page_container = models.OneToOneField(
                              PageContainer,
                              on_delete=models.CASCADE,
                              )
    
    created_at = models.DateTimeField(auto_now_add=True)