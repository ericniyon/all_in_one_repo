# Generated by Django 2.2.7 on 2019-11-28 16:46

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20191125_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='time_zone',
            field=timezone_field.fields.TimeZoneField(default='UTC'),
        ),
    ]
