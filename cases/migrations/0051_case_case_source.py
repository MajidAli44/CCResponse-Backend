# Generated by Django 3.2.8 on 2021-11-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0050_auto_20211123_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_source',
            field=models.CharField(blank=True, choices=[('google', 'Google')], max_length=32, null=True),
        ),
    ]
