# Generated by Django 3.1.4 on 2021-02-24 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='mobileNumber',
        ),
    ]
