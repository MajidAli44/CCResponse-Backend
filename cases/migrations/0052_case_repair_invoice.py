# Generated by Django 3.2.8 on 2021-11-23 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_repairinvoice_repairinvoiceitem'),
        ('cases', '0051_case_case_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='repair_invoice',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoices.repairinvoice'),
        ),
    ]