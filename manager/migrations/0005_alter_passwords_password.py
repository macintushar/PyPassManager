# Generated by Django 4.1.2 on 2022-10-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_passwords_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwords',
            name='password',
            field=models.BinaryField(max_length=1000),
        ),
    ]
