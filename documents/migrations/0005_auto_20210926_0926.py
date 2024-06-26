# Generated by Django 3.2.7 on 2021-09-26 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_documentsignature'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentsignature',
            options={'verbose_name': 'Document signature', 'verbose_name_plural': 'Document signatures'},
        ),
        migrations.RemoveField(
            model_name='documentsignature',
            name='sender',
        ),
        migrations.AddField(
            model_name='documentsignature',
            name='envelope_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='documentsignature',
            name='recipient_name',
            field=models.CharField(default='', max_length=127),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documentsignature',
            name='document',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='document_signature', to='documents.caseuploaddocument'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documentsignature',
            name='recipient',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documentsignature',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('sent', 'Sent'), ('delivered', 'Delivered'), ('signed', 'Signed'), ('completed', 'Completed'), ('declined', 'Declined'), ('voided', 'Voided'), ('deleted', 'Deleted')], default='created', max_length=9),
        ),
    ]
