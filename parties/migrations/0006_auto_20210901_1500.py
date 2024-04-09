# Generated by Django 3.2.6 on 2021-09-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0005_auto_20210812_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdparty',
            name='insurer_contact_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='thirdparty',
            name='insurer_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='thirdparty',
            name='insurer_ref',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]