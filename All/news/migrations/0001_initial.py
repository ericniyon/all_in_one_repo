# Generated by Django 2.2.4 on 2019-08-05 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('album_logo', models.ImageField(upload_to='logo')),
                ('artist', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('song_type', models.CharField(max_length=100)),
                ('song_formt', models.CharField(max_length=20)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Album')),
            ],
        ),
    ]
