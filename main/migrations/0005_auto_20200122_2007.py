# Generated by Django 2.2.9 on 2020-01-23 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200101_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 22, 20, 7, 55, 787951), verbose_name='date published'),
        ),
    ]
