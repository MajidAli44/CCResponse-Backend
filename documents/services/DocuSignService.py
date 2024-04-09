import base64

from django.conf import settings
from docusign_esign import ApiClient, EnvelopeDefinition, Document, Signer, Recipients, EnvelopesApi

from common.services.StorageService import storageService
from documents.document_tabs import client_hire_document_pack_tabs


class DocuSignService(object):
    def __init__(self):
        self.__user_id = settings.DOCUSIGN_USER_ID
        self.__client_id = settings.DOCUSIGN_CLIENT_ID
        self.__account_id = settings.DOCUSIGN_ACCOUNT_ID
        self.__base_path = settings.DOCUSIGN_BASE_PATH
        self.__authorization_server = settings.DOCUSIGN_AUTH_SERVER
        self.__private_key = base64.b64decode(settings.DOCUSIGN_PRIVATE_KEY)

    def _jwt_auth(self):
        api_client = ApiClient()
        api_client.set_base_path(self.__authorization_server)
        use_scopes = ['signature', 'impersonation']

        response = api_client.request_jwt_user_token(
            client_id=self.__client_id,
            user_id=self.__user_id,
            oauth_host_name=self.__authorization_server,
            private_key_bytes=self.__private_key,
            expires_in=3600,
            scopes=use_scopes
        )
        return response.access_token

    def make_envelope(self, document_signature):
        env = EnvelopeDefinition(
            email_subject='Please sign this document'
        )
        if document_signature.message:
            env = EnvelopeDefinition(
                email_subject='Please sign this document',
                email_blurb=document_signature.message
            )
        file_bytes = storageService.get_from_s3_to_bytes(document_signature.document.rel_file_path)
        b64 = base64.b64encode(file_bytes).decode('ascii')
        document_id = document_signature.document_id
        recipient_id = document_signature.document.case.client_id
        document = Document(
            document_base64=b64,
            name=document_signature.document.name,
            file_extension='docx',
            document_id=document_id
        )
        env.documents = [document]
        signer1 = Signer(
            email=document_signature.recipient,
            name=document_signature.recipient_name,
            recipient_id=document_signature.document.case.client_id,
        )
        signer1.tabs = client_hire_document_pack_tabs(
            document_id,
            recipient_id,
            hire_details=document_signature.document.case.hire_detail,
            hire_agreement=document_signature.document.case.hire_agreement
        )
        recipients = Recipients(signers=[signer1])
        env.recipients = recipients
        env.status = 'sent'

        return env

    def create_api_client(self, base_path, access_token):
        """Create api client and construct API headers"""
        api_client = ApiClient()
        api_client.host = base_path
        api_client.set_default_header(header_name='Authorization', header_value=f'Bearer {access_token}')
        return api_client

    def send_via_email(self, document_signature):
        envelope_definition = self.make_envelope(document_signature)
        api_client = self.create_api_client(base_path=self.__base_path, access_token=self._jwt_auth())
        envelope_api = EnvelopesApi(api_client)
        results = envelope_api.create_envelope(account_id=self.__account_id, envelope_definition=envelope_definition)
        return results.envelope_id

    def download_document(self, envelope_id, document_id):
        api_client = self.create_api_client(base_path=self.__base_path, access_token=self._jwt_auth())
        envelope_api = EnvelopesApi(api_client)
        return envelope_api.get_document(self.__account_id, document_id, envelope_id)

    def get_envelope_status(self, envelope_id):
        api_client = self.create_api_client(base_path=self.__base_path, access_token=self._jwt_auth())
        envelope_api = EnvelopesApi(api_client)
        response = envelope_api.get_envelope(self.__account_id, envelope_id)
        return response.status


docusign_service = DocuSignService()
