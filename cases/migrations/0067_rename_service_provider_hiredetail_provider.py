# Generated by Django 3.2.8 on 2023-02-27 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0066_auto_20230227_0454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiredetail',
            old_name='service_provider',
            new_name='provider',
        ),
    ]
