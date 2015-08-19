# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20150817_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]
