# Generated by Django 2.1.4 on 2018-12-28 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaemsungapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search_image',
            old_name='user_id',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user_extrainfo',
            old_name='user_id',
            new_name='User',
        ),
    ]
