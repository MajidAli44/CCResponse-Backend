# Generated by Django 3.2.8 on 2022-02-01 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0062_alter_recoverydetail_recovery_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hireagreement',
            name='hire_reason',
        ),
    ]
