# Generated by Django 5.0.6 on 2024-07-12 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_profile_pro_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pro_pic',
            field=models.ImageField(default='../static/profilepic/default.png', upload_to='profilepic/'),
        ),
    ]
