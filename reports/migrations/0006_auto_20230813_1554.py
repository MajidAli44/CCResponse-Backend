# Generated by Django 3.2.8 on 2023-08-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20230812_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='users_to_email',
        ),
        migrations.AddField(
            model_name='report',
            name='email_addresses',
            field=models.TextField(default=''),
        ),
    ]
