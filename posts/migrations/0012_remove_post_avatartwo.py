# Generated by Django 3.1.4 on 2022-05-10 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_avatartwo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='avatartwo',
        ),
    ]