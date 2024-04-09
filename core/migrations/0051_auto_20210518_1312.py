# Generated by Django 3.2 on 2021-05-18 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20210518_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclerecovery',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recoveries', to='core.case'),
        ),
        migrations.AddField(
            model_name='vehiclestorage',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='storages', to='core.case'),
        ),
    ]