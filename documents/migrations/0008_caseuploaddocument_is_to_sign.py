# Generated by Django 3.2.7 on 2021-10-06 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_caseuploaddocument_is_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseuploaddocument',
            name='is_to_sign',
            field=models.BooleanField(default=False),
        ),
    ]
