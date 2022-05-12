# Generated by Django 3.1.4 on 2022-05-10 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20220510_1106'),
        ('posts', '0006_remove_post_avatartwo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avatartwo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
