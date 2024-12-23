import uuid

from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=99)
    title = models.CharField(max_length=99)
    content = models.TextField()
    published_date = models.DateField()
    is_published = models.BooleanField(default=False, blank=False)
