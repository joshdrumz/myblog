# Generated by Django 2.2.9 on 2020-01-02 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200101_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 1, 23, 45, 28, 474446), verbose_name='date published'),
        ),
    ]
