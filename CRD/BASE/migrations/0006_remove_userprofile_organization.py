# Generated by Django 5.0.1 on 2024-08-12 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BASE', '0005_userprofile_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='organization',
        ),
    ]
