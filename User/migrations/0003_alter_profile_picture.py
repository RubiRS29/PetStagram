# Generated by Django 3.2.5 on 2021-07-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20210716_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='profiles_pictures'),
        ),
    ]
