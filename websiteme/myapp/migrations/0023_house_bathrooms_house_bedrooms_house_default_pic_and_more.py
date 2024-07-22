# Generated by Django 5.0.6 on 2024-07-12 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_profile_pro_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='bathrooms',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='bedrooms',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='default_pic',
            field=models.ImageField(default='property_images/defhouse.jpg', upload_to='property_images/'),
        ),
        migrations.AddField(
            model_name='house',
            name='floors',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='sqft',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='utilities',
            field=models.CharField(default='Standard', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='house',
            name='pics',
            field=models.ImageField(null=True, upload_to='', verbose_name='HouseImage'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pro_pic',
            field=models.ImageField(default='profilepic/default.png', upload_to='profilepic/'),
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images/')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp.house')),
            ],
        ),
    ]
