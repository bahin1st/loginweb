# Generated by Django 5.0.6 on 2024-07-09 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_profile_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profilepic',
        ),
    ]