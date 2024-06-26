# Generated by Django 3.2.7 on 2021-09-19 15:25

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0007_auto_20210913_1304'),
        ('cases', '0029_auto_20210916_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parties.provider'),
        ),
        migrations.AlterField(
            model_name='userdisplaycasecolumn',
            name='columns',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('instruction_date', 'Instruction date'), ('accident_date', 'Accident date'), ('client_name', 'Client name'), ('phone_number', 'Phone number'), ('introducer', 'Introducer'), ('provider', 'Provider'), ('instructed_solicitor', 'Instructed solicitor'), ('tp_insurer', 'Third party insurer')], max_length=20), default=list, size=8),
        ),
    ]
