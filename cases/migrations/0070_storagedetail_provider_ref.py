# Generated by Django 3.2.8 on 2023-02-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0069_hiredetail_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagedetail',
            name='provider_ref',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
