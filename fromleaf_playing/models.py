from django.db import models

from fromleaf_common.models.page import PageContainer

class PlayingPage(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(PlayingPage, self).__init__(*args, **kwargs)

    def __unicode__(self):  # __str__ on Python3
        return self.page_name 
    
    name = 'PlayingPage'
    description = 'this page is Playing page.'    
    page_container = models.OneToOneField(
                              PageContainer,
                              on_delete=models.CASCADE,
                              )
    
    created_at = models.DateTimeField(auto_now_add=True)