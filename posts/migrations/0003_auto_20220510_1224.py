# Generated by Django 3.1.4 on 2022-05-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220510_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
    ]
