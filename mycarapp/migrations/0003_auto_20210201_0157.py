# Generated by Django 3.1.5 on 2021-02-01 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycarapp', '0002_auto_20210201_0041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='rsvoiture',
            new_name='voiture',
        ),
    ]
