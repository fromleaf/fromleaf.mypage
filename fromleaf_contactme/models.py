from __future__ import unicode_literals
from django.db import models

from fromleaf_common.models.page import PageContainer

class ContactMePage(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(ContactMePage, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.name 
    
    name = 'Contact Me Page'
    description = '저에 대해서 궁금하신 점이 있으시면, 아래 폼에 맞춰서 메일 보내주세요.지금 홈페이지에 대한 내용뿐만 아니라, 개발에 대한 궁금증을 보내주셔도 됩니다.'
    page_container = models.OneToOneField(
                                          PageContainer,
                                          on_delete=models.CASCADE,
                                          )
    created_at = models.DateTimeField(auto_now_add=True)    
