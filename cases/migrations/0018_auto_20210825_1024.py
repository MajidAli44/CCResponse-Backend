# Generated by Django 3.2.6 on 2021-08-25 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0017_alter_case_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='followup',
            options={'verbose_name': 'Follow Up', 'verbose_name_plural': 'Follow Ups'},
        ),
        migrations.RemoveField(
            model_name='case',
            name='follow_up',
        ),
        migrations.RemoveField(
            model_name='followup',
            name='follow_up',
        ),
        migrations.AddField(
            model_name='followup',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follow_ups', to='cases.case'),
        ),
        migrations.AddField(
            model_name='followup',
            name='is_resolved',
            field=models.BooleanField(default=False),
        ),
    ]