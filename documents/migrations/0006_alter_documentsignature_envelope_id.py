# Generated by Django 3.2.7 on 2021-09-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_auto_20210926_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentsignature',
            name='envelope_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
