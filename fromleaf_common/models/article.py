from __future__ import unicode_literals
from django.db import models

from fromleaf_studying.models import StudyingPage


def get_upload_to(instance, filename):
    # Dumb proxy to instance method.
    return instance.get_upload_to(filename)

class Article(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)
        
    def __unicode__(self):  # __str__ on Python3
        return self.title
    
    def get_upload_to(self, filename):
        folder_name = 'photos/profile'
        filename = self.profile_image.field.storage.get_valid_name(filename)

        # do a unidecode in the filename and then
        # replace non-ascii characters in filename with _ , to sidestep issues with filesystem encoding
        filename = "".join((i if ord(i) < 128 else '_') for i in unidecode(filename))

        # Truncate filename so it fits in the 100 character limit
        # https://code.djangoproject.com/ticket/9893
        while len(os.path.join(folder_name, filename)) >= 95:
            prefix, dot, extension = filename.rpartition('.')
            filename = prefix[:-1] + dot + extension
        
        return os.path.join(folder_name, filename) 
    
    title = models.CharField(max_length=200, )
    describe = models.TextField(help_text='Input Describe', blank=True)
    code = models.TextField(help_text='Input Code', bank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', max_length=100)
    image = models.ImageField(upload_to=get_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    
    studying_page = models.ForeignKey(
                                StudyingPage,  
                                on_delete=models.CASCADE,
                            )