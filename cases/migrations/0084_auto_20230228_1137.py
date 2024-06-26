# Generated by Django 3.2.8 on 2023-02-28 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0083_auto_20230228_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='PiClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('solicitor_ref', models.CharField(blank=True, max_length=100, null=True)),
                ('fee', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'verbose_name': 'PiClient',
                'verbose_name_plural': 'PiClients',
            },
        ),
        migrations.AddField(
            model_name='pidetail',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.piclient'),
        ),
    ]
