# Generated by Django 3.1.7 on 2021-03-11 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210310_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
    ]