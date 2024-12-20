import uuid

from django.db import models

class Article(models.Model):
    pk = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=99)
    title = models.CharField(max_length=99)
    content = models.TextField()
    published_date = models.DateField()
