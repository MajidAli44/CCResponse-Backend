# Generated by Django 3.1.7 on 2021-04-16 11:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20210415_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='injury',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='injury',
            name='finished_at',
        ),
        migrations.RemoveField(
            model_name='injury',
            name='injury_file',
        ),
        migrations.RemoveField(
            model_name='injury',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='injury',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='injury',
            name='title',
        ),
        migrations.AddField(
            model_name='injury',
            name='case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='injuries', to='core.case'),
        ),
        migrations.AddField(
            model_name='injury',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='injury',
            name='solicitor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='injuries', to='core.externalparty'),
        ),
        migrations.AlterField(
            model_name='injury',
            name='status',
            field=models.CharField(max_length=200),
        ),
    ]
