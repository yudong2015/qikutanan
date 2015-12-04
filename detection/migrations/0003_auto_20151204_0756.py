# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0002_auto_20151204_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawrecord',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reward',
            name='number',
            field=models.CharField(unique=True, max_length=20, verbose_name='\u5956\u5238\u53f7'),
        ),
    ]
