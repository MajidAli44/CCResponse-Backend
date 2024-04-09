# 0098_add_followup_options.py

from django.db import migrations
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

def add_new_choices(apps, schema_editor):
    FollowUp = apps.get_model('your_app_name', 'FollowUp')  # Replace 'your_app_name' with the actual app name

    new_choices = [
        ('liability_vd_chasers', 'Liability/VD Chasers'),
        ('er_client_approval', 'ER Client Approval'),
        ('cases_in_validation', 'Cases in Validation'),
        ('vehicle_collections', 'Vehicle Collections'),
        ('general_follow_up', 'General Follow Up'),
    ]

    for choice_value, choice_label in new_choices:
        FollowUp.TypeChoices.add_item(choice_value, choice_label)

class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0097_alter_case_status_description'),  # Replace 'your_app_name' with actual values
    ]

    operations = [
        # migrations.RunPython(add_new_choices),
    ]
