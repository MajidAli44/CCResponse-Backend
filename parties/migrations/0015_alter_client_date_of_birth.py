# Generated by Django 3.2.8 on 2022-01-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0014_alter_client_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]