# Generated by Django 3.2.5 on 2021-07-20 15:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('ref', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Insurer',
                'verbose_name_plural': 'Insurers',
            },
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, help_text='International format', max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Only international format', regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')])),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('address', models.TextField()),
                ('policy_number', models.CharField(blank=True, max_length=200, null=True)),
                ('other_details', models.TextField(blank=True, null=True)),
                ('insurer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='third_parties', to='parties.insurer')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.thirdpartyvehicle')),
            ],
            options={
                'verbose_name': 'Third party',
                'verbose_name_plural': 'Third parties',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, help_text='International format', max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Only international format', regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')])),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('license_number', models.CharField(blank=True, max_length=50, null=True)),
                ('ni_number', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex='^\\s*[a-zA-Z]{2}(?:\\s*\\d\\s*){6}[a-zA-Z]?\\s*$')])),
                ('insurer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='parties.insurer')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.clientvehicle')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
