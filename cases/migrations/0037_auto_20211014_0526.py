# Generated by Django 3.2.7 on 2021-10-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0036_auto_20211013_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiredetail',
            name='outsourced_vehicle',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hiredetail',
            name='outsourced_vehicle_make_model',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='hiredetail',
            name='outsourced_vehicle_vrn',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
