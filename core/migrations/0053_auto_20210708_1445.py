# Generated by Django 3.2 on 2021-07-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20210707_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Admin?'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Deleted?'),
        ),
    ]
