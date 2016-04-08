import os.path

from django.conf import settings
from django.db import models
from unidecode import unidecode

from fromleaf_common.models.user import UserInfo


class PageContainer(models.Model):
    def __init__(self, *args, **kwargs):
        super(PageContainer, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.title  
    
    user_info = models.OneToOneField(
                              UserInfo,
                              on_delete=models.CASCADE,
                              )
    title = models.CharField(max_length=20, default='page_container')