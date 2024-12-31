import uuid

from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=99)
    title = models.CharField(max_length=99)
    subtitle = models.CharField(max_length=99)
    content = models.TextField()
    published_date = models.DateField()
    is_published = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f"{self.title}: {self.subtitle} by {self.author}"
