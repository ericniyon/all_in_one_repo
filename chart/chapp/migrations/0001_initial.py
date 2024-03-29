# Generated by Django 2.2.7 on 2019-11-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('groupe', models.CharField(choices=[('district', 'district'), ('sector', 'sector')], max_length=10)),
                ('survived', models.BooleanField()),
                ('year', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
