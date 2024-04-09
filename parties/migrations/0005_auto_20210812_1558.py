# Generated by Django 3.2.6 on 2021-08-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0004_auto_20210806_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introducer',
            name='hire_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='introducer',
            name='pi_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='solicitor',
            name='pi_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]