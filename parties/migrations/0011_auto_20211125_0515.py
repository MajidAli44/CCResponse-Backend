# Generated by Django 3.2.8 on 2021-11-25 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0010_auto_20211125_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ni_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, help_text='International format', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='thirdparty',
            name='phone_number',
            field=models.CharField(blank=True, help_text='International format', max_length=50, null=True),
        ),
    ]