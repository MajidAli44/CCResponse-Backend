# Generated by Django 3.2.8 on 2021-10-22 04:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0043_auto_20211021_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdisplaycasecolumn',
            name='columns',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('cc_ref', 'CC Ref'), ('instruction_date', 'Instruction date'), ('accident_date', 'Accident date'), ('client_name', 'Client name'), ('phone_number', 'Phone number'), ('introducer', 'Introducer'), ('provider', 'Provider'), ('instructed_solicitor', 'Instructed solicitor'), ('tp_insurer', 'Third party insurer')], max_length=20), default=list, size=9),
        ),
    ]
