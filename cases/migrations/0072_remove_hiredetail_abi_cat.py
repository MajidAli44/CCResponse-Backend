# Generated by Django 3.2.8 on 2023-02-27 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0071_hiredetail_abi_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiredetail',
            name='abi_cat',
        ),
    ]
