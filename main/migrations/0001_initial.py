# Generated by Django 2.2.9 on 2020-01-01 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(default=datetime.datetime(2019, 12, 31, 19, 13, 29, 861023), verbose_name='date published')),
            ],
        ),
    ]
