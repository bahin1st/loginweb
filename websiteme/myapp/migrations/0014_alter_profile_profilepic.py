# Generated by Django 5.0.6 on 2024-07-09 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(default='default.png', upload_to='profile_pics/'),
        ),
    ]