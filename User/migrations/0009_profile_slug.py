# Generated by Django 3.2.5 on 2021-07-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_profile_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
