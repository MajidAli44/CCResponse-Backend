# Generated by Django 3.2.8 on 2023-02-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0068_auto_20230227_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiredetail',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('pickup', 'Pickup'), ('arranged', 'Arranged')], max_length=20, null=True),
        ),
    ]
