# Generated by Django 3.2.5 on 2021-07-29 01:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, null=True, related_name='_User_profile_follow_+', to=settings.AUTH_USER_MODEL, verbose_name='follow'),
        ),
    ]