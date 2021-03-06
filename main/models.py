from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class TutorialCategory(models.Model):
    category = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/',
                              default=None, blank=True, null=True)
    image_alt = models.CharField(max_length=200, default='')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class TutorialSeries(models.Model):
    series = models.CharField(max_length=200)
    category = models.ForeignKey(
        TutorialCategory, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.series


class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default='placeholder')
    content = models.TextField()
    published = models.DateTimeField(
        verbose_name='date published', default=datetime.now())
    series = models.ForeignKey(
        TutorialSeries, default=1, verbose_name='Series', on_delete=models.SET_DEFAULT)
    slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.title
