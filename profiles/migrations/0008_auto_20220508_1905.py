# Generated by Django 3.1.4 on 2022-05-08 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20220508_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='simple-forum-django-main/media/default.jpg', upload_to='simple-forum-django-main/media/profile_images'),
        ),
    ]
