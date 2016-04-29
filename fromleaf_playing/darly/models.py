from __future__ import unicode_literals

import os.path
import logging

from django.conf import settings
from django.db import models
from unidecode import unidecode

logger = logging.getLogger(__name__)

def get_upload_to(instance, filename):
    # Dumb proxy to instance method.
    return instance.get_upload_to(filename)

class DarlyPhoto(models.Model):
    def __init__(self, *args, **kwargs):
        super(DarlyPhoto, self).__init__(*args, **kwargs)
    
    photo_name = models.CharField(max_length=200)
    #photo = models.ImageField(upload_to=get_upload_to)
    photo = models.ImageField(upload_to=get_upload_to)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_upload_to(self, filename):
        # folder_name = settings.MEDIA_ROOT + '/photos/darly'
        folder_name = 'photos/darly'
        filename = self.photo.field.storage.get_valid_name(filename)

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
    
    def __unicode__(self):  # __str__ on Python3
        return self.photo_name