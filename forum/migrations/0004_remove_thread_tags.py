# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_subforum_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='tags',
        ),
    ]
