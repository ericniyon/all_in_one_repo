# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0005_auto_20150607_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='shown_days',
            field=models.PositiveIntegerField(default=6, verbose_name='Number of days to show in calendar', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7')]),
        ),
    ]
