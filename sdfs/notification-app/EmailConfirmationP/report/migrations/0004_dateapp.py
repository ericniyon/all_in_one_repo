# Generated by Django 2.2.7 on 2019-12-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20191222_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dateapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('deadline', models.DateField()),
            ],
        ),
    ]
