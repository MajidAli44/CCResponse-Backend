# Generated by Django 3.2.8 on 2021-10-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0007_auto_20210913_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='introducer',
            old_name='fee',
            new_name='hire_fee',
        ),
        migrations.AddField(
            model_name='introducer',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='introducer',
            name='company_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='introducer',
            name='contact_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='introducer',
            name='office_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='introducer',
            name='pi_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='solicitor',
            name='contact_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='solicitor',
            name='hotkey_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='solicitor',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitor',
            name='pi_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
