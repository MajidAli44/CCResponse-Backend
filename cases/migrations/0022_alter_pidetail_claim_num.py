# Generated by Django 3.2.6 on 2021-08-29 15:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0021_auto_20210829_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pidetail',
            name='claim_num',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
