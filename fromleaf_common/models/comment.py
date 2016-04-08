from __future__ import unicode_literals
from django.db import models

from fromleaf_aboutme.models import AboutMePage


class SimpleComment(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(SimpleComment, self).__init__(*args, **kwargs)
        
    def __unicode__(self):  # __str__ on Python3
        return self.title
    
    title = models.CharField(max_length=200, )
    comment = models.TextField(help_text='Input Comment')
    created_at = models.DateTimeField(auto_now_add=True)
    
    aboutme_page = models.ForeignKey(
                                AboutMePage,  
                                on_delete=models.CASCADE,
                            )