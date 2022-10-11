# Generated by Django 4.1.2 on 2022-10-11 19:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_article_celebs_remove_blinditem_celebs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1000)),
                ('date_posted', models.DateField(default=datetime.date.today)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main_app.photo')),
            ],
        ),
    ]