# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('display_name', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('post_ptr', models.OneToOneField(to='forum.Post', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('forum.post',),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('post_ptr', models.OneToOneField(to='forum.Post', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('comment', models.ForeignKey(to='forum.Comment')),
            ],
            options={
            },
            bases=('forum.post',),
        ),
        migrations.CreateModel(
            name='Subforum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('subforum_ptr', models.OneToOneField(to='forum.Subforum', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('colloquiums', models.TextField()),
            ],
            options={
            },
            bases=('forum.subforum',),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('subforum_ptr', models.OneToOneField(to='forum.Subforum', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('office_hours', models.TextField()),
                ('mentor_sessions', models.TextField()),
                ('department', models.ForeignKey(to='forum.Department')),
            ],
            options={
            },
            bases=('forum.subforum',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('post_ptr', models.OneToOneField(to='forum.Post', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('title', models.CharField(max_length=128)),
                ('subforum', models.ForeignKey(to='forum.Subforum')),
                ('tags', models.ManyToManyField(to='forum.Tag')),
            ],
            options={
            },
            bases=('forum.post',),
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(to='forum.Thread'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='forums',
            field=models.ManyToManyField(to='forum.Subforum'),
            preserve_default=True,
        ),
    ]
