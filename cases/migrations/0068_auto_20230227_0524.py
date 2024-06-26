# Generated by Django 3.2.8 on 2023-02-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0067_rename_service_provider_hiredetail_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagedetail',
            name='provider',
            field=models.CharField(blank=True, choices=[('cc_response', 'CC Response'), ('copart', 'Copart')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='storagedetail',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('pickup', 'Pickup'), ('arranged', 'Arranged')], max_length=20, null=True),
        ),
    ]
