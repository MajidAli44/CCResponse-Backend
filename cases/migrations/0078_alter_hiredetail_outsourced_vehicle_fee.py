# Generated by Django 3.2.8 on 2023-02-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0077_alter_hiredetail_outsourced_vehicle_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiredetail',
            name='outsourced_vehicle_fee',
            field=models.DecimalField(blank=True, choices=[('400.00', 'Standard'), ('650.00', 'Prestige')], decimal_places=2, max_digits=12, null=True),
        ),
    ]
