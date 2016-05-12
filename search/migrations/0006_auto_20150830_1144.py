# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20150818_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='abbr',
            field=models.CharField(default='TJ', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
