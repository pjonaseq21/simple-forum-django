# Generated by Django 3.1.4 on 2022-05-10 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220510_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='avatar',
            new_name='avatartwo',
        ),
    ]