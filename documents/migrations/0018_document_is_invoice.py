# Generated by Django 3.2.8 on 2021-11-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0017_auto_20211027_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_invoice',
            field=models.BooleanField(default=False),
        ),
    ]