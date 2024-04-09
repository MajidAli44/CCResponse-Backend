# Generated by Django 3.1.7 on 2021-03-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_scheduledtochasecase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='follow_up',
        ),
        migrations.RemoveField(
            model_name='case',
            name='follow_up_date',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='owner',
            field=models.CharField(choices=[('customer', 'Customer'), ('third_party', 'Third Party'), ('company', 'Company')], db_index=True, default='company', max_length=20),
        ),
    ]