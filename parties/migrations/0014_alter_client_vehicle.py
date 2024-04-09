# Generated by Django 3.2.8 on 2022-01-05 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0006_vehiclefieldsdefaultprice'),
        ('parties', '0013_alter_client_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client', to='vehicles.clientvehicle'),
        ),
    ]