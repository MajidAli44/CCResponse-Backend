# Generated by Django 3.1.6 on 2021-02-25 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210222_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='chat',
            name='unique_chat',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='introducer_fee',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_third_party',
        ),
        migrations.RemoveField(
            model_name='user',
            name='license_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ni_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='make',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='model',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='policy_number',
        ),
        migrations.AddField(
            model_name='case',
            name='communication',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='externalpartyservice',
            name='introducer_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='is_worker_sender',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='make_and_model',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('party_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.party')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('license_number', models.CharField(blank=True, max_length=100)),
                ('ni_number', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=200)),
            ],
            bases=('core.party',),
        ),
        migrations.CreateModel(
            name='ExternalParty',
            fields=[
                ('party_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.party')),
                ('role', models.CharField(choices=[('insurer', 'Insurer'), ('introducer', 'Introducer'), ('solicitor', 'Solicitor')], max_length=50)),
                ('ref', models.CharField(blank=True, max_length=200)),
                ('is_third_party', models.BooleanField(default=False)),
                ('introducer_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
            options={
                'verbose_name_plural': 'External parties',
            },
            bases=('core.party',),
        ),
        migrations.AddField(
            model_name='chat',
            name='party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='party_chats', to='core.party'),
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('party_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.party')),
                ('policy_number', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('insurer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='insurer_third_parties', to='core.externalparty')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_third_parties', to='core.vehicle')),
            ],
            options={
                'verbose_name_plural': 'Third parties',
            },
            bases=('core.party',),
        ),
        migrations.AddField(
            model_name='case',
            name='third_party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='third_party_cases', to='core.thirdparty'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_bookings', to='core.customer'),
        ),
        migrations.AlterField(
            model_name='case',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_cases', to='core.customer'),
        ),
        migrations.AlterField(
            model_name='case',
            name='external_parties',
            field=models.ManyToManyField(related_name='external_party_cases', through='core.ExternalPartyService', to='core.ExternalParty'),
        ),
        migrations.AlterField(
            model_name='externalpartyservice',
            name='external_party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='external_party_services', to='core.externalparty'),
        ),
        migrations.AlterField(
            model_name='injury',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='injuries', to='core.customer'),
        ),
        migrations.AddConstraint(
            model_name='chat',
            constraint=models.UniqueConstraint(fields=('worker', 'party', 'type'), name='unique_chat'),
        ),
    ]
