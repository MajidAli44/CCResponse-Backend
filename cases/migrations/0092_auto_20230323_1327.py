# Generated by Django 3.2.8 on 2023-03-23 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0091_auto_20230322_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='title',
            field=models.CharField(choices=[('follow_up', 'Follow up'), ('insurer_chase', 'Insurer chase'), ('client_update', 'Client update')], default='follow_up', max_length=55),
        ),
        migrations.AddField(
            model_name='followup',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CaseTask',
        ),
    ]
