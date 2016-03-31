from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class BlogPost(models.Model):
    text = models.TextField()
    image = models.ImageField(blank=True)
    author = models.ForeignKey("users.BlogUser")
    publish_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def __unicode__(self):
        return "Post from {} (author: {})".format(self.created_at, self.author)
