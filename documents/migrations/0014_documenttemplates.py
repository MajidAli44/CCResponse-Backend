# Generated by Django 3.2.8 on 2021-10-22 08:35

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0044_alter_userdisplaycasecolumn_columns'),
        ('documents', '0013_documentsignature'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTemplates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('empty_fields', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), blank=True, default=list, null=True, size=None)),
                ('document_need_sign', models.BooleanField(default=False)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_templates', to='cases.case')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_templates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Document template',
                'verbose_name_plural': 'Documents templates',
            },
        ),
    ]
