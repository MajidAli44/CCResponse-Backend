from documents.generators import LetterHeadDocumentGenerator, StatementOfTruthDocumentGenerator, \
    WitnessStatementDocumentGenerator, NewClaimNotificationDocumentGenerator, \
    ReleaseNoteMansfieldGroupDocumentGenerator, ReleaseNoteMotorMoveUKDocumentGenerator, \
    LetterClientOnConclusionClaimDocumentGenerator, VehicleExcessDueDamageDocumentGenerator, \
    WitnessRequestingStatementDocumentGenerator, NoticeRightCancelDocumentGenerator, \
    RepairsSatisfactionNoteDocumentGenerator, HirePackDocumentGenerator, LetterClientPAVDocumentGenerator, \
    NewClaimFormDocumentGenerator, PaymentPackDocumentGenerator, RepairInvoiceDocumentGenerator

LETTER_HEAD = 'Letter Head'
NEW_CLAIM_NOTIFICATION = 'New Claim Notification'
RELEASE_NOTE_MANSFIELD_GROUP = 'Release Note Mansfield Group'
RELEASE_NOTE_MOTOR_MOVE_UK = 'Release Note Motor Move UK'
LETTER_TO_CLIENT_ON_CONCLUSION_OF_CLAIM = 'Letter to Client on Conclusion of Claim'
LETTER_TO_CLIENT_VEHICLE_EXCESS_DUE_TO_DAMAGE = 'Letter to Client Vehicle Excess Due to Damage'
LETTER_TO_WITNESS_REQUESTING_STATEMENT = 'Letter to Witness Requesting Statement'
NOTICE_OF_RIGHT_TO_CANCEL = 'Notice of Right to Cancel'
CLIENT_VEHICLE_REPAIRS_SATISFACTION_NOTE = 'Client Vehicle Repairs Satisfaction Note'
CLIENT_HIRE_DOCUMENT_PACK = 'Client Hire Document Pack and Care Letters'
LETTER_TO_CLIENT_WITH_PAV = 'Letter to Client with PAV'
STATEMENT_OF_TRUTH = 'Statement of Truth'
WITNESS_STATEMENT = 'Witness Statement'
NEW_CLAIM_FORM = 'New Claim Form'
PAYMENT_PACK = 'Payment Pack'
REPAIR_INVOICE = 'Repair Invoice'

DOCUMENT_FIELDS = {
    LETTER_HEAD: {
        'filename': 'Letter Head.docx',
        'generator': LetterHeadDocumentGenerator,
        'is_to_sign': False,
    },
    STATEMENT_OF_TRUTH: {
        'filename': 'Statement of Truth.docx',
        'generator': StatementOfTruthDocumentGenerator,
        'is_to_sign': False,
    },
    WITNESS_STATEMENT: {
        'filename': 'Witness Statement.pdf',
        'generator': WitnessStatementDocumentGenerator,
        'is_to_sign': False,
    },
    NEW_CLAIM_NOTIFICATION: {
        'filename': 'New Claim Notification.docx',
        'generator': NewClaimNotificationDocumentGenerator,
        'is_to_sign': False,
    },
    RELEASE_NOTE_MANSFIELD_GROUP: {
        'filename': 'Release Note Mansfield Group.docx',
        'generator': ReleaseNoteMansfieldGroupDocumentGenerator,
        'is_to_sign': False,
    },
    RELEASE_NOTE_MOTOR_MOVE_UK: {
        'filename': 'Release Note Motor Move UK.docx',
        'generator': ReleaseNoteMotorMoveUKDocumentGenerator,
        'is_to_sign': False,
    },
    LETTER_TO_CLIENT_ON_CONCLUSION_OF_CLAIM: {
        'filename': 'Letter to Client on Conclusion of Claim.docx',
        'generator': LetterClientOnConclusionClaimDocumentGenerator,
        'is_to_sign': False,
    },
    LETTER_TO_CLIENT_VEHICLE_EXCESS_DUE_TO_DAMAGE: {
        'filename': 'Letter to Client Vehicle Excess Due to Damage.docx',
        'generator': VehicleExcessDueDamageDocumentGenerator,
        'is_to_sign': False,
    },
    LETTER_TO_WITNESS_REQUESTING_STATEMENT: {
        'filename': 'Letter to Witness Requesting Statement.docx',
        'generator': WitnessRequestingStatementDocumentGenerator,
        'is_to_sign': False,
    },
    NOTICE_OF_RIGHT_TO_CANCEL: {
        'filename': 'Notice of Right to Cancel.docx',
        'generator': NoticeRightCancelDocumentGenerator,
        'is_to_sign': False,
    },
    CLIENT_VEHICLE_REPAIRS_SATISFACTION_NOTE: {
        'filename': 'Client Vehicle Repairs Satisfaction Note.docx',
        'generator': RepairsSatisfactionNoteDocumentGenerator,
        'is_to_sign': False,
    },
    CLIENT_HIRE_DOCUMENT_PACK: {
        'filename': 'Client Hire Document Pack and Care Letters.docx',
        'generator': HirePackDocumentGenerator,
        'is_to_sign': True,
    },
    LETTER_TO_CLIENT_WITH_PAV: {
        'filename': 'Letter to Client with PAV.docx',
        'generator': LetterClientPAVDocumentGenerator,
        'is_to_sign': False,
    },
    NEW_CLAIM_FORM: {
        'filename': 'New Claim Form.docx',
        'generator': NewClaimFormDocumentGenerator,
        'is_to_sign': False,
    },
    PAYMENT_PACK: {
        'filename': 'Payment Pack.docx',
        'generator': PaymentPackDocumentGenerator,
        'is_to_sign': False,
    },
    REPAIR_INVOICE: {
        'filename': 'Repair Invoice.docx',
        'generator': RepairInvoiceDocumentGenerator,
        'is_to_sign': False
    }
}
