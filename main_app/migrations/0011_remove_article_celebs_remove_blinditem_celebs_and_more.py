# Generated by Django 4.1.2 on 2022-10-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_video_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='celebs',
        ),
        migrations.RemoveField(
            model_name='blinditem',
            name='celebs',
        ),
        migrations.RemoveField(
            model_name='messageboard',
            name='celebs',
        ),
        migrations.RemoveField(
            model_name='video',
            name='celebs',
        ),
        migrations.AddField(
            model_name='article',
            name='celeb',
            field=models.ManyToManyField(to='main_app.celeb'),
        ),
        migrations.AddField(
            model_name='blinditem',
            name='celeb',
            field=models.ManyToManyField(to='main_app.celeb'),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='celeb',
            field=models.ManyToManyField(to='main_app.celeb'),
        ),
        migrations.AddField(
            model_name='video',
            name='celeb',
            field=models.ManyToManyField(to='main_app.celeb'),
        ),
    ]