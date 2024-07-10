# Generated by Django 5.0.6 on 2024-07-09 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_profile_firstname_profile_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address_line',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='phonenumber',
            field=models.IntegerField(blank=True, default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='postcode',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='state_region',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]