import os.path
import logging

from django.db import models
from unidecode import unidecode


def get_upload_to(instance, filename):
    # Dumb proxy to instance method.
    return instance.get_upload_to(filename)


class MemberInfo(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(MemberInfo, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.email    
    
    GUEST = 'GUEST'
    MEMBER = 'MEMBER'
    OWNER = 'OWNER'
    ADMIN = 'ADMIN'
    
    MEMBER_CHOICES = (
        (GUEST, 'Guest'),
        (MEMBER, 'Member'),
        (OWNER, 'Owner'),
        (ADMIN, 'Administrator'),
    )
    
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    grade = models.CharField(
                             max_length=10, 
                             choices=MEMBER_CHOICES,
                             default=MEMBER
                             )
    created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add 옵션 : 데이터가 “처음” 만들어 질 때
                                                            # auto_now 옵션 : 데이터가 저장 될 때
    
    
class ExtraUserInfo(models.Model):
    def __init__(self, *args, **kwargs):
        super(ExtraUserInfo, self).__init__(*args, **kwargs)
        
    def get_upload_to(self, filename):
        folder_name = 'photos/profile/'
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
    
    name = models.CharField(max_length=100)
    birthday = models.DateField(default='1980-01-01')
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.PositiveIntegerField(blank=True)
    cellphone_number = models.PositiveIntegerField(blank=True)
    profile_image = models.ImageField(upload_to=get_upload_to, blank=True)
    blog_address = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add 옵션 : 데이터가 “처음” 만들어 질 때
                                                            # auto_now 옵션 : 데이터가 저장 될 때
                                                            
    member_info = models.OneToOneField(
                              MemberInfo,
                              on_delete=models.CASCADE,
                              )
    

class UserSNSInfo(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(UserSNSInfo, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.user_id  
            
    FACEBOOK = 'FACEBOOK'
    GITHUB = 'GITHUB'
    LINKEDIN = 'LINKEDIN'
 
    SERVICE_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (GITHUB, 'Github'),
        (LINKEDIN, 'Linkedin'),
    )
    
    sns_name =  models.CharField(max_length=200, choices=SERVICE_CHOICES)
    sns_address = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    
    extra_user_info = models.ForeignKey(
                              'ExtraUserInfo',
                              on_delete=models.CASCADE,
                              )
    



class Education(models.Model):
    def __init__(self, *args, **kwargs):
        super(Education, self).__init__(*args, **kwargs)
        
    def __unicode__(self):  # __str__ on Python3
        return self.name 
    
    ELEMENTARY_SCHOOL = 'ELEMENTARY_SCHOOL'
    MIDDLE_SCHOOL = 'MIDDLE_SCHOOL'
    HIGH_SCHOOL = 'HIGH_SCHOOL'
    UNIVERSICY = 'UNIVERSICY'
    GRADUATE_SCHOOL = 'GRADUATE_SCHOOL'
    
    SCHOOL_CHOICES = (
        (ELEMENTARY_SCHOOL, 'Elementary School'),
        (MIDDLE_SCHOOL, 'Middle School'),
        (HIGH_SCHOOL, 'High School'),
        (UNIVERSICY, 'University'),
        (GRADUATE_SCHOOL, 'Graduate school')
    )
    
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=50, choices=SCHOOL_CHOICES)
    major = models.CharField(max_length=200, null=True)
    score = models.FloatField(default=0.0, blank=True)
    entranced_date = models.DateField(default='1980-01-01', null=True)
    graduated_date = models.DateField(default='1980-01-01', null=True)
    
    extra_user_info = models.ForeignKey(
                                        'ExtraUserInfo',
                                        on_delete=models.CASCADE,
                                    )
                                                            