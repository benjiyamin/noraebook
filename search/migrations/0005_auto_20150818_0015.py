# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_song_is_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_approved',
            new_name='approved',
        ),
    ]
