# Generated by Django 3.2.6 on 2021-08-10 12:19

from decimal import Decimal

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0008_alter_case_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoveryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('recovery_date', models.DateField(blank=True, null=True)),
                ('recovery_type', models.CharField(blank=True, choices=[('standard', 'Standard'), ('out_of_hours', 'Out of hours'), ('would_not_drive_steer_roll', 'Would not drive/Steer/Roll'), ('crane_four_wheel_lift_required', 'Crane/Four wheel lift required')], max_length=50, null=True)),
                ('other_recovery_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('call_out_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('winching_time', models.CharField(blank=True, choices=[('null', 'null'), ('minutes_30', '30 Minutes'), ('hour_1', '1 Hour')], max_length=50, null=True)),
                ('road_cleanup', models.BooleanField(blank=True, null=True)),
                ('inherited_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('skates', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='case',
            name='recovery_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.recoverydetail'),
        ),
    ]
