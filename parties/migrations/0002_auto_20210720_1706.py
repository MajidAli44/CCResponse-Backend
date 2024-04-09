# Generated by Django 3.2.5 on 2021-07-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introducer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(blank=True, max_length=50, null=True)),
                ('ref', models.CharField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, max_length=127, null=True)),
                ('company_number', models.CharField(blank=True, max_length=127, null=True)),
                ('office_number', models.CharField(blank=True, max_length=127, null=True)),
                ('pi_fee', models.PositiveIntegerField(blank=True, null=True)),
                ('hire_fee', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Introducer',
                'verbose_name_plural': 'Introducers',
            },
        ),
        migrations.CreateModel(
            name='Solicitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(blank=True, max_length=50, null=True)),
                ('ref', models.CharField(blank=True, max_length=255, null=True)),
                ('hotkey_number', models.CharField(blank=True, max_length=127, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('pi_fee', models.PositiveIntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Solicitor',
                'verbose_name_plural': 'Solicitors',
            },
        ),
        migrations.RenameField(
            model_name='insurer',
            old_name='phone_number',
            new_name='contact_number',
        ),
    ]