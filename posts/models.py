from email.mime import image
import imp
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from unittest.util import _MAX_LENGTH


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    likecount = models.IntegerField(
        'like_count', default=0, blank=True
    )
    image = CloudinaryField(
        'image', blank =True ,db_index = True
    )
