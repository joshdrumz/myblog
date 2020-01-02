from django.db import models
from datetime import datetime

# Create your models here.


class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default='placeholder')
    content = models.TextField()
    published = models.DateTimeField(
        verbose_name='date published', default=datetime.now())

    def __str__(self):
        return self.title
