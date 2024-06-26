# Generated by Django 3.1.7 on 2021-04-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20210416_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='injury',
            name='type',
            field=models.CharField(choices=[('rta', 'RTA'), ('trip_slip', 'Trip Slip'), ('aaw', 'AAW')], default='rta', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='injury',
            name='status',
            field=models.CharField(choices=[('need_to_hotkey', 'Need to hotkey'), ('hotkeyed', 'Hotkeyed'), ('paid_also', 'Paid Also')], max_length=15),
        ),
    ]
