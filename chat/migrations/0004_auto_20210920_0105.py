# Generated by Django 3.2.7 on 2021-09-20 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='twilio_message_sid',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='twilio_message_status',
            field=models.CharField(blank=True, choices=[('sent', 'Sent'), ('received', 'Received'), ('read', 'Read')], max_length=8, null=True),
        ),
        migrations.AddIndex(
            model_name='chatmessage',
            index=models.Index(fields=['twilio_message_sid'], name='chat_chatme_twilio__f790a2_idx'),
        ),
    ]
