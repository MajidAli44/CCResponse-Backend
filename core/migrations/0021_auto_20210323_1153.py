# Generated by Django 3.1.7 on 2021-03-23 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20210323_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledtochasecase',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_to_chase_case', to='core.case'),
        ),
    ]
