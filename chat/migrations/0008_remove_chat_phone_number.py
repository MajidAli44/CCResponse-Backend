# Generated by Django 3.2.7 on 2021-09-22 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_chatmessage_twilio_message_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='phone_number',
        ),
    ]
