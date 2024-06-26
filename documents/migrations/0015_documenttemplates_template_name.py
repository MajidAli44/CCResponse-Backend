# Generated by Django 3.2.8 on 2021-10-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0014_documenttemplates'),
    ]

    operations = [
        migrations.AddField(
            model_name='documenttemplates',
            name='template_name',
            field=models.CharField(blank=True, choices=[('Letter Head', 'Letter Head'), ('New Claim Notification', 'New Claim Notification'), ('Release Note Mansfield Group', 'Release Note Mansfield Group'), ('Release Note Motor Move UK', 'Release Note Motor Move UK'), ('Letter to Client on Conclusion of Claim', 'Letter to Client on Conclusion of Claim'), ('Letter to Client Vehicle Excess Due to Damage', 'Letter to Client Vehicle Excess Due to Damage'), ('Letter to Witness Requesting Statement', 'Letter to Witness Requesting Statement'), ('Notice of Right to Cancel', 'Notice of Right to Cancel'), ('Client Vehicle Repairs Satisfaction Note', 'Client Vehicle Repairs Satisfaction Note'), ('Client Hire Document Pack and Care Letters', 'Client Hire Document Pack and Care Letters'), ('Letter to Client with PAV', 'Letter to Client with PAV'), ('Statement of Truth', 'Statement of Truth'), ('Witness Statement', 'Witness Statement'), ('New Claim Form', 'New Claim Form'), ('Payment Pack', 'Payment Pack')], max_length=128, null=True),
        ),
    ]
