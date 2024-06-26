# Generated by Django 3.2.8 on 2021-11-17 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0045_alter_case_instruction_date'),
        ('chat', '0009_auto_20210923_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_read', models.BooleanField(default=False)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='cases.case')),
                ('chat_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='chat.chatmessage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]
