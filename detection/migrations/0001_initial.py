# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DrawRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=100)),
                ('user', models.OneToOneField(related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('remain', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='reward',
            name='type',
            field=models.ForeignKey(related_name='rewards', to='detection.Rewards'),
        ),
        migrations.AddField(
            model_name='drawrecord',
            name='reward',
            field=models.ForeignKey(related_name='draw', to='detection.Reward'),
        ),
        migrations.AddField(
            model_name='drawrecord',
            name='user',
            field=models.OneToOneField(related_name='draw', to=settings.AUTH_USER_MODEL),
        ),
    ]
