# Generated by Django 2.2.7 on 2019-12-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_report_time_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reported_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
