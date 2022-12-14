# Generated by Django 4.1.2 on 2022-10-09 14:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_photo_date_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlindItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.CharField(max_length=1000)),
                ('date_posted', models.DateField(default=datetime.date.today)),
                ('celebs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blind', to='main_app.celeb')),
            ],
        ),
    ]
