# Generated by Django 3.1.4 on 2022-05-19 16:14

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20220519_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format=None, keep_meta=True, quality=-1, size=[10, 10], upload_to='profile_images'),
        ),
    ]
