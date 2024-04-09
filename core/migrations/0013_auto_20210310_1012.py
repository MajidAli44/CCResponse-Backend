# Generated by Django 3.1.7 on 2021-03-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210309_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='settlement_status',
            field=models.CharField(blank=True, choices=[('unsettled', 'Unsettled'), ('settled', 'Settled')], default='unsettled', max_length=100),
        ),
    ]
