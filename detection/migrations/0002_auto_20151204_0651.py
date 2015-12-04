# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='remain',
            field=models.IntegerField(default=100, verbose_name='\u5269\u4f59\u5956\u5238\u603b\u6570'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reward',
            name='number',
            field=models.CharField(max_length=20, verbose_name='\u5956\u5238\u53f7'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='password',
            field=models.CharField(max_length=20, verbose_name='\u5956\u5238\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='type',
            field=models.CharField(max_length=50, verbose_name='\u5956\u52b1\u7c7b\u578b'),
        ),
        migrations.DeleteModel(
            name='Rewards',
        ),
    ]
