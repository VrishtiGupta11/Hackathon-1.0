# Generated by Django 2.2.10 on 2021-03-05 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='location',
            new_name='item',
        ),
    ]
