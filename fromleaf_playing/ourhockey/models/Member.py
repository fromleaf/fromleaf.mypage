from __future__ import unicode_literals

import logging
import os.path

from django.db import models
from unidecode import unidecode

from fromleaf_playing.ourhockey.models.GameDay import GameDay

logger = logging.getLogger(__name__)

# ImageField는 FileField를 상속받는데 upload_to 옵션에서 함수를 넣으면, instance랑 filename을 보낸다. 신기한녀석이다, 
def get_upload_to(instance, filename):
    # Dumb proxy to instance method.
    return instance.get_upload_to(filename)

class Person(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.name
    
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    member = models.OneToOneField('Member', on_delete=models.CASCADE, primary_key=True)

  
class Player(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        player_info = position + '_' + str(back_number)
        return player_info
                 
    back_number = models.IntegerField(default=0, unique=True)
    position = models.CharField(max_length=100)
    member = models.OneToOneField('Member', on_delete=models.CASCADE, primary_key=True)
       
       
class Member(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(Member, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        if self.level is 0:
            return 'Not Member'
        elif self.level in [1, 2]:
            return 'PreMember'
        elif self.level is 3:
            return 'Member'
        elif self.level is 4:
            return 'Official'
        else:
            return 'Not Member'

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
    profile_image = models.ImageField(upload_to=get_upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    
class Attendance(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(Attendance, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        if self.attended is True:
            return 'Attended'
        else:
            return 'Not Attended'
        
    attended = models.BooleanField()
    attended_date = models.DateField(auto_now=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE, null=True)
    