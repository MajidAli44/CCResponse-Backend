# Generated by Django 3.1.7 on 2021-03-29 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20210323_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledtochasecase',
            name='user_last_scheduled',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
