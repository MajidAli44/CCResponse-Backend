from django.contrib import admin
from ccresponse import settings

from core.admin import AttachmentAdmin, CaseAdmin, CaseDocumentAdmin, CaseNoteAdmin, ChatAdmin, CustomerAdmin, \
    DocumentTemplateAdmin, ExpenseAdmin, ExternalPartyAdmin, InjuryAdmin, InstructEngineerAdmin, InvoiceAdmin, \
    MessageAdmin, NotificationAdmin, ThirdPartyAdmin, UserAdmin, VehicleAdmin, VehicleHireAdmin, \
    VehicleRecoveryAdmin, VehicleStorageAdmin
from core.models import RegistrationVerifyRequest, PasswordResetRequest, EmailVerifyRequest

if settings.DEBUG:
    admin.site.register(RegistrationVerifyRequest)
    admin.site.register(PasswordResetRequest)
    admin.site.register(EmailVerifyRequest)

__all__ = [
    'AttachmentAdmin', 'CaseAdmin', 'CaseDocumentAdmin', 'CaseNoteAdmin', 'ChatAdmin', 'CustomerAdmin',
    'DocumentTemplateAdmin', 'ExpenseAdmin', 'ExternalPartyAdmin', 'InjuryAdmin', 'InstructEngineerAdmin',
    'InvoiceAdmin', 'MessageAdmin', 'NotificationAdmin', 'ThirdPartyAdmin', 'UserAdmin', 'VehicleAdmin',
    'VehicleHireAdmin', 'VehicleRecoveryAdmin', 'VehicleStorageAdmin',
]
