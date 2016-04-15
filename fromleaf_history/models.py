from __future__ import unicode_literals
from django.db import models

from fromleaf_common.models.page import PageContainer

def get_upload_to(instance, filename):
    # Dumb proxy to instance method.
    return instance.get_upload_to(filename)

class HistoryPage(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(HistoryPage, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.page_name 
    
    page_name = 'HistoryPage'
    page_describe = 'This page is History Page.'    
    page_container = models.OneToOneField(
                              PageContainer,
                              on_delete=models.CASCADE,
                              )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Company(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(Company, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.name
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    history_page = models.ForeignKey(
                              'HistoryPage',
                              on_delete=models.CASCADE,
                              null=True
                              )

class Project(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.title
    
    def get_upload_to(self, filename):
        folder_name = 'photos/architecture/'
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
    
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200, blank=True)
    system = models.CharField(max_length=200, blank=True)
    framework = models.CharField(max_length=200, blank=True)
    architecture = models.ImageField(upload_to=get_upload_to, blank=True)
    architecture_describe = models.CharField(max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    company = models.ForeignKey(
                              'Company',
                              on_delete=models.CASCADE,
                              )


