# Generated by Django 4.2.2 on 2023-07-14 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_remove_jobpost_duration_jobpost_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(default='0im39r'),
        ),
    ]
