# Generated by Django 3.2.6 on 2021-08-23 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_hirevehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_date', models.DateField(blank=True, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('hire_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='vehicles.hirevehicle')),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
    ]