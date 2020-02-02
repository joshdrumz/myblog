# Generated by Django 2.2.9 on 2020-02-01 23:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200122_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialcategory',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 1, 18, 30, 34, 629670), verbose_name='date published'),
        ),
    ]
