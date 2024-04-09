# Generated by Django 3.2.8 on 2023-06-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0096_alter_case_status_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='status_description',
            field=models.CharField(blank=True, choices=[('lead_new_lead', 'New Lead'), ('lead_no_answer', 'No Answer'), ('lead_awaiting_further_info', 'Await more Info'), ('lead_hk_to_provider', 'HK to Provider'), ('ongoing_accepted', 'Accepted'), ('ongoing_in_hire', 'In hire'), ('payment_pack_pp_issued', 'PP Submitted'), ('payment_pack_settlement_agreed', 'Settlement Agreed'), ('payment_pack_passed_to_ra', 'Litigated'), ('settled_closed_no_contact', 'Closed - Failed Contact'), ('settled_closed_poor_prospects', 'Closed - Poor Prospects'), ('settled_closed_client_dwtp', 'Client DWTP'), ('settled_closed_abandoned_recovery', 'Abandoned Recovery'), ('settled_closed_file_settled', 'File Settled')], default='lead_awaiting_further_info', max_length=50, null=True),
        ),
    ]
