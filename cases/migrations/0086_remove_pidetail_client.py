# Generated by Django 3.2.8 on 2023-02-28 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0085_auto_20230228_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pidetail',
            name='client',
        ),
    ]
