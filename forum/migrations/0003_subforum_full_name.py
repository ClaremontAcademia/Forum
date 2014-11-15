# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20141115_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='subforum',
            name='full_name',
            field=models.CharField(max_length=128, default='CS Department'),
            preserve_default=False,
        ),
    ]
