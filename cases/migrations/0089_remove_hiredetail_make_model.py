# Generated by Django 3.2.8 on 2023-03-04 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0088_alter_case_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiredetail',
            name='make_model',
        ),
    ]