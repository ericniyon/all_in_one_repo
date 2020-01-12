# Generated by Django 2.2.7 on 2020-01-03 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesOfReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=300)),
                ('igihe_itangirwa', models.PositiveSmallIntegerField(choices=[(1, 'Icyumweru'), (2, 'Ukwezi'), (3, 'Igihembwe'), (4, 'Amezi atandatu'), (5, 'Umwaka')], help_text='eg: Icyumweru, Ukwezi etc..')),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Department')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_file', models.FileField(upload_to='reports')),
                ('submitted_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('report_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportapp.TypesOfReport')),
            ],
        ),
    ]
