# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jisho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definition',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
