# Generated by Django 3.0 on 2020-11-19 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0004_auto_20201118_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='idPublicacion',
            new_name='id',
        ),
    ]
