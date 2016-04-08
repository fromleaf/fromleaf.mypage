import os.path

from django.db import models
from unidecode import unidecode


def get_upload_to(instance, filename):
    # Dumb proxy to instance method.
    return instance.get_upload_to(filename)


class MemberInfo(models.Model):
    def __init__(self, *args, **kwargs):
        super(MemberInfo, self).__init__(*args, **kwargs)

    def set_member_info(self, **kwargs):
        self.email = kwargs['email']
        self.password = kwargs['password']
        self.grade = kwargs['grade']
        self.user_info = kwargs['user_info']
    
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
    user_info = models.OneToOneField(
                              'UserInfo',
                              on_delete=models.CASCADE,
                              )
    
    
class ExtraUserInfo(models.Model):
    def __init__(self, *args, **kwargs):
        super(ExtraUserInfo, self).__init__(*args, **kwargs)
        
    def set_extra_user_info(self, **kwargs):
        self.address = kwargs['address']
        self.phone_number = kwargs['phone_number']
        self.cellphone_number = kwargs['phone_number']
        self.profile_image = kwargs['profile_image']
        self.blog_address = kwargs['blog_address']
        self.user_info = kwargs['user_info']
        
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
    
    address = models.CharField(max_length=200)
    phone_number = models.PositiveIntegerField()
    cellphone_number = models.PositiveIntegerField()
    profile_image = models.ImageField(upload_to=get_upload_to)
    blog_address = models.URLField(max_length=200)
    
    user_info = models.OneToOneField(
                              'UserInfo',
                              on_delete=models.CASCADE,
                              )
    

class UserSNSInfo(models.Model):
    def __init__(self, *args, **kwargs):
        super(UserSNSInfo, self).__init__(*args, **kwargs) 
        
    github_id = models.CharField(max_length=200)
    github_address = models.URLField(max_length=200)
    facebook_id = models.CharField(max_length=200)
    facebook_address = models.URLField(max_length=200)
    linkedin_id = models.CharField(max_length=200)
    linkedin_address = models.URLField(max_length=200)
    
    extra_user_info = models.OneToOneField(
                              'ExtraUserInfo',
                              on_delete=models.CASCADE,
                              )
    
    
class UserInfo(models.Model):
    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        
    def set_user(self, **kwargs):
        self.name = kwargs['name']
        self.birthday = kwargs['birthday']
    
    def __unicode__(self):  # __str__ on Python3
        return self.name  
    
    name = models.CharField(max_length=100)
    birthday = models.DateField(default='1980-01-01')
    created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add 옵션 : 데이터가 “처음” 만들어 질 때
                                                            # auto_now 옵션 : 데이터가 저장 될 때
                                                            