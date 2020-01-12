# Generated by Django 3.0 on 2019-12-22 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_dateapp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dateapp',
        ),
        migrations.AddField(
            model_name='reporttype',
            name='initial_date',
            field=models.DateField(default=datetime.date(2019, 11, 1)),
        ),
        migrations.AlterField(
            model_name='reporttype',
            name='deadline',
            field=models.DateField(),
        ),
    ]
