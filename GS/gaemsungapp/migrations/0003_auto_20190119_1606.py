# Generated by Django 2.1.4 on 2019-01-19 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaemsungapp', '0002_auto_20181228_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search_image',
            old_name='latitude',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='search_image',
            name='longtitude',
        ),
    ]
