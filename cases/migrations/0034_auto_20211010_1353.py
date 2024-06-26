# Generated by Django 3.2.7 on 2021-10-10 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0033_case_instruct_engineer_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='HireValidation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('engs_instructed', models.DateField(blank=True, null=True)),
                ('inspection_date', models.DateField(blank=True, null=True)),
                ('report_received', models.DateField(blank=True, null=True)),
                ('sent_to_tp', models.DateField(blank=True, null=True)),
                ('repairable', models.BooleanField(default=False)),
                ('total_loss_cil', models.BooleanField(default=False)),
                ('repair_auth', models.DateField(blank=True, null=True)),
                ('sat_note_sign', models.DateField(blank=True, null=True)),
                ('settle_offer', models.DateField(blank=True, null=True)),
                ('offer_accepted', models.DateField(blank=True, null=True)),
                ('cheque_received', models.DateField(blank=True, null=True)),
                ('liability_admitted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Hire validation',
                'verbose_name_plural': 'Hire validations',
            },
        ),
        migrations.RemoveField(
            model_name='case',
            name='instruct_engineer_date',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='act_completion',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='booking_in_date',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='engs_instructed',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='est_completion_date',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='liability_admitted',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='rep_cost_outlay',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='rep_inv_amt',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='rep_inv_vat',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='rep_pay_received',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='repairs_started',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='report_received',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='returned_to_customer',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='sent_to_tp',
        ),
        migrations.RemoveField(
            model_name='hiredetail',
            name='tp_auth_received',
        ),
        migrations.AddField(
            model_name='case',
            name='hire_validation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.hirevalidation'),
        ),
    ]
