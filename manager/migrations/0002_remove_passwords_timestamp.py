# Generated by Django 4.1.2 on 2022-10-19 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwords',
            name='timestamp',
        ),
    ]
