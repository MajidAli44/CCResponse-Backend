# Generated by Django 3.2.6 on 2021-09-03 12:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0026_casefieldsdefaultprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='instruction_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
