# Generated by Django 3.2.8 on 2021-11-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0009_auto_20211125_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='insurer',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='thirdparty',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='thirdparty',
            name='insurer_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
