# Generated by Django 3.1.7 on 2021-04-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_casedocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casedocument',
            name='file',
            field=models.FileField(storage='storages.backends.s3boto3.S3Boto3Storage', upload_to='case_documents'),
        ),
    ]