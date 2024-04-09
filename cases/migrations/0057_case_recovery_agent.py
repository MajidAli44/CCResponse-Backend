# Generated by Django 3.2.8 on 2021-11-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0056_hirevalidation_liability_admitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='recovery_agent',
            field=models.CharField(blank=True, choices=[('cc_response', 'CC Response'), ('canfords', 'Canfords'), ('barings', 'Barings'), ('dgm', 'DGM')], max_length=32, null=True),
        ),
    ]