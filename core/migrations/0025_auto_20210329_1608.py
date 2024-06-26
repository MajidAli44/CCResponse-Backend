# Generated by Django 3.1.7 on 2021-03-29 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_merge_20210329_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='vehicle_hire',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice', to='core.vehiclehire'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vehicle_recovery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice', to='core.vehiclerecovery'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vehicle_storage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice', to='core.vehiclestorage'),
        ),
    ]
