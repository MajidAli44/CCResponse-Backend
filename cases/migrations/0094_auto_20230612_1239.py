# Generated by Django 3.2.8 on 2023-06-12 12:39

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0093_alter_case_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='hire_detail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hire_details', to='cases.hiredetail'),
        ),
        migrations.AlterField(
            model_name='case',
            name='services',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('cd', 'Claim Details'), ('hd', 'Hire Details'), ('sr', 'Storage Recovery'), ('pi', 'Personal Injury'), ('vd', 'Vehicle Damage'), ('sv', 'Salvage')], max_length=20), default=['cd'], size=6),
        ),
    ]