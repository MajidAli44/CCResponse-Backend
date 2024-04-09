# Generated by Django 3.1.6 on 2021-02-17 07:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210213_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('externalpartyservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.externalpartyservice')),
            ],
            bases=('core.externalpartyservice',),
        ),
        migrations.RemoveField(
            model_name='case',
            name='instruction_date',
        ),
        migrations.RemoveField(
            model_name='externalpartyservice',
            name='dated_retained',
        ),
        migrations.RemoveField(
            model_name='externalpartyservice',
            name='follow_up',
        ),
        migrations.RemoveField(
            model_name='externalpartyservice',
            name='follow_up_date',
        ),
        migrations.RemoveField(
            model_name='externalpartyservice',
            name='instruction_date',
        ),
        migrations.RemoveField(
            model_name='externalpartyservice',
            name='introducer_fee',
        ),
        migrations.RemoveField(
            model_name='externalpartyservice',
            name='notes',
        ),
        migrations.AddField(
            model_name='case',
            name='follow_up',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='case',
            name='follow_up_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='tp_other_details',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='externalpartyservice',
            name='finish_work_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='externalpartyservice',
            name='joined_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='externalpartyservice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('ongoing', 'Rejected by Sols'), ('payment_pack', 'Clawback'), ('settled', 'Paid')], default='ongoing', max_length=30),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_paid',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Introducer',
            fields=[
                ('externalpartyservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.externalpartyservice')),
                ('introducer_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
            bases=('core.externalpartyservice',),
        ),
        migrations.CreateModel(
            name='Solicitor',
            fields=[
                ('externalpartyservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.externalpartyservice')),
                ('instruction_date', models.DateField(blank=True, null=True)),
                ('date_retained', models.DateField(blank=True, null=True)),
            ],
            bases=('core.externalpartyservice',),
        ),
    ]