# Generated by Django 3.2 on 2021-07-07 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_auto_20210518_1312'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
