from twilio.rest import Client

from ccresponse import settings


class WhatsAppService:

    message_templates = {
        'initialize_chat': 'Dear <client_name>, this is <manager_name> from CC Response. We’ve been instructed to handle your accident case. Please respond to this message to initiate the chat.',
        'intro_message': 'Hi There, Please respond to this message to initiate the chat. Thanks, CC Response - 01616390141'
    }

    def __init__(self, twilio_account_sid: str, twilio_auth_token: str):
        self.twilio_account_sid = 'AC885dad3cbcf6015eefa3c4237b28b970'
        self.twilio_auth_token = '18464584404f8e0ac49861e857e57a7e'

        self.twilio_client = Client(self.twilio_account_sid, self.twilio_auth_token)

    def send_template_message(self, phone_number: str, template_name: str, **kwargs):
        print("Phone numner is---",phone_number)
        if template_name not in self.message_templates:
            raise ValueError(f'The template {template_name} not found')

        template = self.message_templates[template_name]
        for arg, value in kwargs.items():
            template = template.replace(f'<{arg}>', value)

        if '<' in template and '>' in template:
            raise ValueError('The message template is not fully filled in')
        print("template My number---",settings.TWILIO_ACCOUNT_SENDER_NUMBER)
        print("template To send---",phone_number)
        return self.twilio_client.messages.create(
            body=template, from_=f'whatsapp:{"+14155238886"}', to=f'whatsapp:{phone_number}'
        )

    def send_text_message(self, phone_number: str, content: str):
        print("My number---",settings.TWILIO_ACCOUNT_SENDER_NUMBER)
        print("To send---",phone_number)
        return self.twilio_client.messages.create(
            from_=f'whatsapp:{settings.TWILIO_ACCOUNT_SENDER_NUMBER}', to=f'whatsapp:{phone_number}', body=content
        )

    def send_file_message(self, phone_number: str, content: str):
        return self.twilio_client.messages.create(
            from_=f'whatsapp:{settings.TWILIO_ACCOUNT_SENDER_NUMBER}', to=f'whatsapp:{phone_number}', media_url=content
        )
