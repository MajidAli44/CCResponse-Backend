# Generated by Django 3.2.8 on 2023-02-27 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_hirevehicle_abi_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hirevehicle',
            name='abi_cat',
        ),
    ]
