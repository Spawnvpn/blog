from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class BlogUser(AbstractUser):
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        return super(BlogUser, self).save(*args, **kwargs)
