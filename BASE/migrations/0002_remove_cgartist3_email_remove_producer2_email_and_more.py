# Generated by Django 5.0.1 on 2024-04-24 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BASE', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cgartist3',
            name='email',
        ),
        migrations.RemoveField(
            model_name='producer2',
            name='email',
        ),
        migrations.RemoveField(
            model_name='supervisor2',
            name='email',
        ),
    ]
