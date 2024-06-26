# Generated by Django 3.2.8 on 2021-11-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0046_alter_accident_circumstances'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='status_description',
            field=models.CharField(blank=True, choices=[('lead_no_answer', 'No Answer'), ('load_awaiting_further_info', 'Awaiting further info'), ('lead_hk_to_provider', 'load hk to provider'), ('ongoing_accepted', 'Accepted'), ('ongoing_in_hire', 'In hire'), ('payment_pack_pp_issued', 'PP Issued'), ('payment_pack_settlement_agreed', 'Settlement Agreed'), ('payment_pack_passed_to_ra', 'Passed to RA'), ('settled_closed_no_contact', 'settled closed no contact'), ('settled_closed_poor_prospects', 'settled closed poor prospects'), ('settled_closed_client_dwtp', 'settled closed client dwtp'), ('settled_closed_abandoned_recovery', 'settled closed abandoned recovery'), ('settled_closed_file_settled', 'settled closed file settled')], max_length=50, null=True),
        ),
    ]
