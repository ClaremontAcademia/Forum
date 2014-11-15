# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_remove_thread_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
