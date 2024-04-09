# Generated by Django 3.2.7 on 2021-09-17 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0029_auto_20210916_1206'),
        ('chat', '0002_auto_20210917_0621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('whats_app_chat_status', models.CharField(choices=[('client', 'Inactive'), ('manager', 'Pending'), ('active', 'Active')], default='client', max_length=8)),
                ('whats_app_last_client_message_time', models.DateTimeField(blank=True, null=True)),
                ('whats_app_last_message_time', models.DateTimeField(blank=True, null=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='cases.case')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
