# Generated by Django 3.2 on 2021-05-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20210501_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='should_show_hire_sr',
            field=models.BooleanField(default=False),
        ),
    ]
