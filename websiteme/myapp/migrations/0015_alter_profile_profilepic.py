# Generated by Django 5.0.6 on 2024-07-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(default='D:\\loginweb\\websiteme\\static\\profilepic\\default.png', upload_to='D:\\loginweb\\websiteme\\static\\profilepic/proof.png'),
        ),
    ]
