from __future__ import unicode_literals

import logging
import os.path

from django.db import models
from unidecode import unidecode

logger = logging.getLogger(__name__)

def get_upload_to(instance, filename):
    # Dumb proxy to instance method.
    return instance.get_upload_to(filename)

class Person(models.Model):
    
    def __unicode__(self):  # __str__ on Python3
        return self.name
    
    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    
    player = models.ForeignKey(
                              'Player',
                              on_delete=models.CASCADE,
                              )

  
class Player(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
                 
    back_number = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
       
       
class Member(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(Member, self).__init__(*args, **kwargs)
        
    def get_upload_to(self, filename):
        folder_name = 'photos/ourhockey/profiles'
        filename = self.profile_image.field.storage.get_valid_name(filename)

        # do a unidecode in the filename and then
        # replace non-ascii characters in filename with _ , to sidestep issues with filesystem encoding
        filename = "".join((i if ord(i) < 128 else '_') for i in unidecode(filename))

        # Truncate filename so it fits in the 100 character limit
        # https://code.djangoproject.com/ticket/9893
        while len(os.path.join(folder_name, filename)) >= 95:
            prefix, dot, extension = filename.rpartition('.')
            filename = prefix[:-1] + dot + extension
        # return filename
        return os.path.join(folder_name, filename)
    
    duty = models.CharField(max_length=100)
    level = models.IntegerField(default=0)
    status = models.CharField(max_length=2, default="00")  # 00: alive / 01: Pause / 02: Not attend
    profile_image = models.ImageField(upload_to=get_upload_to,  
                                      null=True)
    player = models.ForeignKey(
                              'Player',
                              on_delete=models.CASCADE,
                              null=True
                              )