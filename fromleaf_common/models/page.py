import os.path

from django.conf import settings
from django.db import models
from unidecode import unidecode

from fromleaf_common.models.user import User


class PageData(models.Model):
    def __init__(self, *args, **kwargs):
        super(PageData, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.title  
    
    #created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
                              User,
                              on_delete=models.CASCADE,
                              )
    title = models.CharField(max_length=20, default='page_data')