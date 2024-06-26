# Generated by Django 3.2.6 on 2021-08-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0009_auto_20210810_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pidetail',
            name='ack_comms',
        ),
        migrations.AddField(
            model_name='pidetail',
            name='claim_num',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pidetail',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='cdw',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='charge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='engineers_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='hire_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='ns_drive_charge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='recovery_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='rep_cost_outlay',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='rep_inv_amt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='rep_inv_vat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='storage_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='hiredetail',
            name='vehicle',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='pidetail',
            name='claim_type',
            field=models.CharField(blank=True, choices=[('rta', 'RTA'), ('aaw', 'AAW'), ('ol', 'OL'), ('pl', 'PL')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recoverydetail',
            name='call_out_charge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='recoverydetail',
            name='inherited_fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='storagedetail',
            name='engineers_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='storagedetail',
            name='fee_per_day',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
