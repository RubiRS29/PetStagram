# Generated by Django 3.2.5 on 2021-07-27 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_userfollowings'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfollowings',
            name='value',
            field=models.CharField(choices=[('Follow', 'Follow'), ('Unfollow', 'Unfollow')], default='Unfollow', max_length=10),
        ),
    ]
