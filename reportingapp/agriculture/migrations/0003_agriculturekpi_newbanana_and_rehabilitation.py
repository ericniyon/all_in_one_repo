# Generated by Django 2.2.2 on 2019-11-29 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20191120_1601'),
        ('agriculture', '0002_auto_20191126_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgricultureKPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Agriculture KPI',
                'verbose_name_plural': 'Agriculture KPIs',
            },
        ),
        migrations.CreateModel(
            name='NewBanana_and_Rehabilitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.PositiveIntegerField()),
                ('achieved', models.PositiveIntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriculture.AgricultureKPI')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Sector')),
            ],
            options={
                'verbose_name': 'new Banana and Rehabilitation',
                'verbose_name_plural': ' new Banana and Rehabilitation',
            },
        ),
    ]
