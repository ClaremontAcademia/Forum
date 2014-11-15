# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subforum',
            name='name',
            field=models.CharField(max_length=16, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=32, unique=True),
            preserve_default=True,
        ),
    ]
