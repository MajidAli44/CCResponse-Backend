# Generated by Django 3.2.8 on 2021-11-17 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0045_alter_case_instruction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='circumstances',
            field=models.CharField(blank=True, choices=[('hir', 'HIR'), ('tp_pulled_from_sr', 'TP pulled from SR'), ('roundabout_accident', 'Roundabout accident'), ('lane_change', 'Lane change'), ('tp_pulled_from_parked_position', 'TP pulled from parked position'), ('reversing_accident', 'Reversing accident'), ('car_par_accident', 'Car park accident'), ('other', 'Other')], max_length=50, null=True),
        ),
    ]
