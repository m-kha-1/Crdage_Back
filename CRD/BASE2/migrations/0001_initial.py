# Generated by Django 5.0.1 on 2024-08-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stockage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('media_root', models.CharField(max_length=50)),
                ('media_url', models.CharField(max_length=50)),
            ],
        ),
    ]
