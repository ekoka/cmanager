# Generated by Django 2.2.9 on 2020-01-22 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date',
            new_name='date_of_contact',
        ),
    ]
