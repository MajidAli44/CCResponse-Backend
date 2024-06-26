# Generated by Django 3.2.5 on 2021-08-02 14:37

from decimal import Decimal

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0003_auto_20210729_1840'),
        ('cases', '0004_auto_20210729_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('follow_up', models.CharField(blank=True, choices=[('need_to_hotkey', 'Need to Hotkey'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('paid', 'Paid')], max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('communication', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StorageDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('fee_per_day', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('engineers_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='case',
            old_name='clawback_details',
            new_name='clawback_detail',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='hire_details',
            new_name='hire_detail',
        ),
        migrations.RemoveField(
            model_name='case',
            name='ack_comms',
        ),
        migrations.RemoveField(
            model_name='case',
            name='communication',
        ),
        migrations.RemoveField(
            model_name='case',
            name='status',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='global_settlement',
        ),
        migrations.CreateModel(
            name='PIDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('claim_type', models.CharField(blank=True, max_length=50, null=True)),
                ('instructed_paid_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('ongoing', 'Ongoing'), ('payment_pack', 'Payment Pack'), ('settled', 'Settled')], max_length=50, null=True)),
                ('ack_comms', models.BooleanField(default=False)),
                ('solicitor_introduced', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parties.solicitor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='case',
            name='pi_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.pidetail'),
        ),
        migrations.AddField(
            model_name='case',
            name='storage_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.storagedetail'),
        ),
    ]
