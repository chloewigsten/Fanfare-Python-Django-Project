# Generated by Django 4.1.2 on 2022-10-10 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_remove_photo_celebs_photo_celebs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='celebs',
            new_name='celeb',
        ),
    ]
