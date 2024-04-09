# Generated by Django 3.2.7 on 2021-10-19 13:20

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0041_alter_userdisplaycasecolumn_columns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casefieldsdefaultprice',
            name='recovery_detail_road_cleanup',
            field=models.DecimalField(decimal_places=2, default=Decimal('25'), max_digits=12),
        ),
    ]
