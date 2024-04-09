import datetime

from cases.models import HireAgreement, HireDetail


def client_hire_document_pack_tabs(document_id, recipient_id, hire_details: HireDetail, hire_agreement: HireAgreement):
    group_a_checked_first = 'false'
    group_a_checked_second = 'false'
    group_a_locked = 'true'
    if hire_agreement.offer_received is not None:
        group_a_checked_first = 'true' if hire_agreement.offer_received == HireAgreement.HireAgreementOfferReceivedStatuses.not_received else 'false'
        group_a_checked_second = 'true' if hire_agreement.offer_received == HireAgreement.HireAgreementOfferReceivedStatuses.received else 'false'

    group_c_locked_first = 'true'
    group_c_checked_first = 'false'
    if hire_agreement.personally_liable is not None:
        group_c_checked_first = 'true' if hire_agreement.personally_liable else 'false'

    group_c_locked_second = 'true'
    group_c_checked_second = 'false'
    if hire_agreement.vehicle_unroadworthy is not None:
        group_c_checked_second = 'true' if hire_agreement.vehicle_unroadworthy else 'false'

    group_c_locked_third = 'true'
    group_c_check_third = 'false'
    if hire_agreement.no_another_vehicle is not None:
        group_c_check_third = 'true' if hire_agreement.no_another_vehicle else 'false'

    group_e_check_a_first = 'false'
    group_e_check_a_second = 'true'
    group_e_check_a_locked = 'true'
    if hire_agreement.prosecution is not None:
        group_e_check_a_first = 'true' if hire_agreement.prosecution == True else 'false'
        group_e_check_a_second = 'true' if hire_agreement.prosecution == False else 'false'

    group_e_check_b_first = 'false'
    group_e_check_b_second = 'true'
    group_e_check_b_locked = 'true'
    if hire_agreement.accident_loss_in_3_past_years is not None:
        group_e_check_b_first = 'true' if hire_agreement.accident_loss_in_3_past_years == True else 'false'
        group_e_check_b_second = 'true' if hire_agreement.accident_loss_in_3_past_years == False else 'false'

    group_e_check_c_locked = 'true'
    group_e_check_c_first = 'false'
    group_e_check_c_second = 'true'
    if hire_agreement.proposal_declined_or_increased_fees is not None:
        group_e_check_c_first = 'true' if hire_agreement.proposal_declined_or_increased_fees == True else 'false'
        group_e_check_c_second = 'true' if hire_agreement.proposal_declined_or_increased_fees == False else 'false'

    group_e_check_d_first = 'false'
    group_e_check_d_second = 'true'
    group_e_check_d_locked = 'true'
    if hire_agreement.diseases is not None:
        group_e_check_d_first = 'true' if hire_agreement.diseases == True else 'false'
        group_e_check_d_second = 'true' if hire_agreement.diseases == False else 'false'

    reason_text = " "
    if hire_details.ns_driver_reason == HireDetail.NSDriverReason.age:
        reason_text = "Age (under 25 or older than 70)"
    elif hire_details.ns_driver_reason == HireDetail.NSDriverReason.occupation:
        reason_text = "Occupation (driver is in one of the following groups: Professional – Sportsmen/Women, Actors, Entertainers, Gamblers and Musicians, Publicans, Journalists)"
    elif hire_details.ns_driver_reason == HireDetail.NSDriverReason.driving_licence:
        reason_text = "Held a full driving licence in the UK for less than 12 months"
    elif hire_details.ns_driver_reason == HireDetail.NSDriverReason.convictions_points:
        reason_text = "Convictions/points (Driver has convictions resulting in an unspent ban or 7 or more outstanding points in the last 4 years)"

    return {
        "signHereTabs": [
            {
                "stampType": "signature",
                "name": "SignHere",
                "tabLabel": "Signature e4452996-f697-4c9c-96c3-4695e398e58c",
                "scaleValue": "0.72",
                "optional": "false",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "3",
                "xPosition": "117",
                "yPosition": "417",
                "tabId": "c7038f8e-c43c-4a41-a539-22abeb4c43c1",
                "tabType": "signhere"
            },
            {
                "stampType": "signature",
                "name": "SignHere",
                "tabLabel": "Signature 40a2f7a7-d67e-49db-a1d0-50b61b9e9714",
                "scaleValue": "0.7307692",
                "optional": "false",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "4",
                "xPosition": "172",
                "yPosition": "654",
                "tabId": "d621255c-6a4d-4fe9-9bac-8866f4eb70b3",
                "tabType": "signhere"
            },
            {
                "stampType": "signature",
                "name": "SignHereOptional",
                "tabLabel": "Signature 6489a3fc-7c74-4a77-98f4-1fdeb432abec",
                "scaleValue": "0.5",
                "optional": "false",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "6",
                "xPosition": "109",
                "yPosition": "611",
                "tabId": "2fb69a59-f142-4767-a6b5-9146f7023ada",
                "tabType": "signhereoptional"
            },
            {
                "stampType": "signature",
                "name": "SignHere",
                "tabLabel": "Signature b127dfd3-d70f-49c0-842b-feeff60b5da6",
                "scaleValue": "0.5",
                "optional": "false",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "6",
                "xPosition": "405",
                "yPosition": "612",
                "tabId": "87b0a94c-7f82-408a-b55f-8231e099f7e6",
                "tabType": "signhere"
            },
            {
                "stampType": "signature",
                "name": "SignHereOptional",
                "tabLabel": "Signature e5527285-5889-4f1e-b6ec-d2beb1cfdffc",
                "scaleValue": "0.5",
                "optional": "false",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "6",
                "xPosition": "403",
                "yPosition": "721",
                "tabId": "aa24f3e4-8338-4045-adda-7bb2694f0a66",
                "tabType": "signhere"
            },
            {
                "stampType": "signature",
                "name": "SignHere",
                "tabLabel": "Signature 8254e78b-45ed-45c6-bee4-c5e3001e2ad6",
                "scaleValue": "0.6",
                "optional": "false",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "7",
                "xPosition": "126",
                "yPosition": "737",
                "tabId": "ee286268-e273-4143-9a72-ba3c9c367775",
                "tabType": "signhere"
            }
        ],
        "initialHereTabs": [
            {
                "name": "InitialHere",
                "tabLabel": "Initial fd4d0ee0-0d2c-4e35-94d0-ed5a048ff897",
                "scaleValue": "0.5588235",
                "optional": "false",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "5",
                "xPosition": "285",
                "yPosition": "345",
                "tabId": "c7533acd-be15-4979-a543-4ad6a2f3d6ed",
                "tabType": "initialhere"
            }
        ],
        "dateSignedTabs": [

        ],

        "textTabs": [
            {
                "validationPattern": "",
                "validationMessage": "",
                "shared": "false",
                "requireInitialOnSharedChange": "false",
                "requireAll": "false",
                "required": "false",
                "locked": "true",
                "concealValueOnDocument": "false",
                "disableAutoSize": "false",
                "maxLength": "4000",
                "tabLabel": "\\*Text 7a2c1924-a965-4ea1-aeb6-a7b6ff3af8ff",
                "font": "lucidaconsole",
                "fontColor": "black",
                "fontSize": "size9",
                "localePolicy": {},
                "value": reason_text,
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "3",
                "xPosition": "55",
                "yPosition": "242",
                "width": "540",
                "height": "127",
                "tabId": "645b37d9-0044-4f91-81a0-d08451ff10e9",
                "tabType": "text"
            },
            {
                "name": "DateSigned",
                "tabLabel": "Date Signed d400d02c-3f01-4b9b-ba6b-333b127df8a5",
                "font": "lucidaconsole",
                "fontColor": "black",
                "fontSize": "size9",
                "localePolicy": {},
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "7",
                "xPosition": "451",
                "yPosition": "744",
                "value": datetime.date.today().strftime("%d/%m/%Y"),
                "width": "0",
                "height": "0",
                "tabId": "fee7b138-6dea-4d39-9516-636b7fa767b5",
                "tabType": "datesigned"
            }
        ],
        "checkboxTabs": [
            {
                "name": "",
                "tabLabel": "Checkbox e88c7ed7-6770-4e6e-95e1-361a47ecc5a2",
                "selected": group_c_checked_first,
                "shared": "false",
                "requireInitialOnSharedChange": "false",
                "font": "lucidaconsole",
                "fontColor": "black",
                "fontSize": "size9",
                "required": "false",
                "locked": group_c_locked_first,
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "2",
                "xPosition": "512",
                "yPosition": "566",
                "width": "0",
                "height": "0",
                "tabId": "1b054441-7345-49fb-b0c8-1dce7f1a5969",
                "tabType": "checkbox",
                "tabGroupLabels": [
                    "Checkbox Group 195070a8-1e92-433c-be0d-012cff0eaa1b"
                ]
            },
            {
                "name": "",
                "tabLabel": "Checkbox 17dbacff-5aeb-405f-91d7-f27ed0f7b2e4",
                "selected": group_c_checked_second,
                "shared": "false",
                "requireInitialOnSharedChange": "false",
                "font": "lucidaconsole",
                "fontColor": "black",
                "fontSize": "size9",
                "required": "false",
                "locked": group_c_locked_second,
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "2",
                "xPosition": "512",
                "yPosition": "653",
                "width": "0",
                "height": "0",
                "tabId": "ac0fc5e2-2dbf-4ede-952b-aa0917013a82",
                "tabType": "checkbox",
                "tabGroupLabels": [
                    "Checkbox Group 7699ad55-cf09-4685-9688-d77ed5f4c00b"
                ]
            },
            {
                "name": "",
                "tabLabel": "Checkbox e984a208-3ad4-4c9d-87bb-ef11614eb325",
                "selected": group_c_check_third,
                "shared": "false",
                "requireInitialOnSharedChange": "false",
                "font": "lucidaconsole",
                "fontColor": "black",
                "fontSize": "size9",
                "required": "false",
                "locked": group_c_locked_third,
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "2",
                "xPosition": "512",
                "yPosition": "688",
                "width": "0",
                "height": "0",
                "tabId": "a0c321d6-8cc2-4ca8-9e7b-c9bc10f4954e",
                "tabType": "checkbox",
                "tabGroupLabels": [
                    "Checkbox Group bc7876b4-0aae-40a2-8dae-521f88f46b1e"
                ]
            },
        ],
        "radioGroupTabs": [
            {
                "documentId": document_id,
                "recipientId": recipient_id,
                "groupName": "Radio Group 61fef274-cbd7-47cf-a682-d390fb1b3030",
                "radios": [
                    {
                        "pageNumber": "2",
                        "xPosition": "513",
                        "yPosition": "427",
                        "value": "Radio1",
                        "selected": group_a_checked_first,
                        "tabId": "aa0e0cb7-af8e-448f-b966-052a31b25762",
                        "required": "true",
                        "locked": group_a_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    },
                    {
                        "pageNumber": "2",
                        "xPosition": "513",
                        "yPosition": "490",
                        "value": "Radio2",
                        "selected": group_a_checked_second,
                        "tabId": "b7d97b44-141c-4491-b626-662a15622dd5",
                        "required": "true",
                        "locked": group_a_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    }
                ],
                "shared": "false",
                "requireInitialOnSharedChange": "false",
                "requireAll": "false",
                "tabType": "radiogroup"
            },
            {
                "documentId": document_id,
                "recipientId": recipient_id,
                "groupName": "Radio Group 1c322371-f721-40cc-85ea-4d4235272f6b",
                "radios": [
                    {
                        "pageNumber": "6",
                        "xPosition": "248",
                        "yPosition": "385",
                        "value": "Radio1",
                        "selected": group_e_check_a_first,
                        "tabId": "9c3f1e28-1d00-4bb3-9cd1-9ee5cb166c21",
                        "required": "false",
                        "locked": group_e_check_a_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    },
                    {
                        "pageNumber": "6",
                        "xPosition": "284",
                        "yPosition": "385",
                        "value": "Radio2",
                        "selected": group_e_check_a_second,
                        "tabId": "eed77f79-3840-491b-b397-da58433ddeac",
                        "required": "false",
                        "locked": group_e_check_a_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    }
                ],
                "shared": "false",
                "requireInitialOnSharedChange": "false",
                "requireAll": "false",
                "tabType": "radiogroup"
            },
            {
                "documentId": document_id,
                "recipientId": recipient_id,
                "groupName": "Radio Group f7f64b4d-a09a-46de-b0c7-48a9d540854a",
                "radios": [
                    {
                        "pageNumber": "6",
                        "xPosition": "248",
                        "yPosition": "415",
                        "value": "Radio2",
                        "selected": group_e_check_b_first,
                        "tabId": "d8e6b424-be85-4047-b8d5-306aae98a754",
                        "required": "false",
                        "locked": group_e_check_b_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    },
                    {
                        "pageNumber": "6",
                        "xPosition": "284",
                        "yPosition": "415",
                        "value": "Radio2",
                        "selected": group_e_check_b_second,
                        "tabId": "72e6b219-0646-48f4-8360-5d4700a015b5",
                        "required": "false",
                        "locked": group_e_check_b_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    }
                ],
                "shared": "false",
                "requireInitialOnSharedChange": "false",
                "requireAll": "false",
                "tabType": "radiogroup"
            },
            {
                "documentId": document_id,
                "recipientId": recipient_id,
                "groupName": "Radio Group c3acc7c7-8a8c-4a37-bb24-44acdaff1e02",
                "radios": [
                    {
                        "pageNumber": "6",
                        "xPosition": "248",
                        "yPosition": "446",
                        "value": "Radio2",
                        "selected": group_e_check_c_first,
                        "tabId": "831a3385-8c64-47d7-8bcf-50d5bdc59424",
                        "required": "false",
                        "locked": group_e_check_c_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    },
                    {
                        "pageNumber": "6",
                        "xPosition": "284",
                        "yPosition": "446",
                        "value": "Radio2",
                        "selected": group_e_check_c_second,
                        "tabId": "306cb510-511e-4a48-8b28-fa707fb81198",
                        "required": "false",
                        "locked": group_e_check_c_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    }
                ],
                "shared": "false",
                "requireInitialOnSharedChange": "false",
                "requireAll": "false",
                "tabType": "radiogroup"
            },
            {
                "documentId": document_id,
                "recipientId": recipient_id,
                "groupName": "Radio Group 97ac4d40-0204-44a4-a41a-b975902dc202",
                "radios": [
                    {
                        "pageNumber": "6",
                        "xPosition": "248",
                        "yPosition": "483",
                        "value": "Radio2",
                        "selected": group_e_check_d_first,
                        "tabId": "a1bf6d2f-4c01-4b6c-88b0-4a7938fa6cc6",
                        "required": "false",
                        "locked": group_e_check_d_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    },
                    {
                        "pageNumber": "6",
                        "xPosition": "284",
                        "yPosition": "483",
                        "value": "Radio2",
                        "selected": group_e_check_d_second,
                        "tabId": "0a971b15-b2b0-471e-aac1-97ce44446399",
                        "required": "false",
                        "locked": group_e_check_d_locked,
                        "font": "lucidaconsole",
                        "bold": "false",
                        "italic": "false",
                        "underline": "false",
                        "fontColor": "black",
                        "fontSize": "size9"
                    }
                ],
                "shared": "false",
                "requireInitialOnSharedChange": "false",
                "requireAll": "false",
                "tabType": "radiogroup"
            }
        ],

        "tabGroups": [
            {
                "groupLabel": "Checkbox Group 195070a8-1e92-433c-be0d-012cff0eaa1b",
                "minimumRequired": "0",
                "maximumAllowed": "1",
                "groupRule": "SelectAtLeast",
                "tabScope": "Document",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "1",
                "xPosition": "0",
                "yPosition": "0",
                "tabId": "b8224a25-6795-4ea0-ada1-c3a970623bf5",
                "tabType": "tabgroup"
            },
            {
                "groupLabel": "Checkbox Group 7699ad55-cf09-4685-9688-d77ed5f4c00b",
                "minimumRequired": "0",
                "maximumAllowed": "1",
                "groupRule": "SelectAtLeast",
                "tabScope": "Document",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "1",
                "xPosition": "0",
                "yPosition": "0",
                "tabId": "b47a7266-7ac1-439f-805f-d38f46e546c3",
                "tabType": "tabgroup"
            },
            {
                "groupLabel": "Checkbox Group bc7876b4-0aae-40a2-8dae-521f88f46b1e",
                "minimumRequired": "0",
                "maximumAllowed": "1",
                "groupRule": "SelectAtLeast",
                "tabScope": "Document",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "1",
                "xPosition": "0",
                "yPosition": "0",
                "tabId": "4e528ab2-9810-4896-8163-7be32364766a",
                "tabType": "tabgroup"
            },
            {
                "groupLabel": "Checkbox Group 59784ccf-8fd3-4ddf-9ad2-7d397b2ae025",
                "minimumRequired": "0",
                "maximumAllowed": "1",
                "groupRule": "SelectAtLeast",
                "tabScope": "Document",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "1",
                "xPosition": "0",
                "yPosition": "0",
                "tabId": "20fea928-c368-4cac-84ae-b4f1a568be49",
                "tabType": "tabgroup"
            },
            {
                "groupLabel": "Checkbox Group 79a6b688-b95b-488c-a856-87c0c0f80693",
                "minimumRequired": "0",
                "maximumAllowed": "1",
                "groupRule": "SelectAtLeast",
                "tabScope": "Document",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "1",
                "xPosition": "0",
                "yPosition": "0",
                "tabId": "89cdac9a-9bfe-4701-ae90-a99be506583a",
                "tabType": "tabgroup"
            },
            {
                "groupLabel": "Checkbox Group 2347b04e-f486-47c6-a411-2b6572a6880e",
                "minimumRequired": "0",
                "maximumAllowed": "1",
                "groupRule": "SelectAtLeast",
                "tabScope": "Document",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "1",
                "xPosition": "0",
                "yPosition": "0",
                "tabId": "6146caa9-3509-4889-b342-ae959f57f14a",
                "tabType": "tabgroup"
            },
            {
                "groupLabel": "Checkbox Group 51f22bea-87af-4bb3-b14a-530a8a3c3b52",
                "minimumRequired": "0",
                "maximumAllowed": "1",
                "groupRule": "SelectAtLeast",
                "tabScope": "Document",
                "documentId": document_id,
                "recipientId": recipient_id,
                "pageNumber": "1",
                "xPosition": "0",
                "yPosition": "0",
                "tabId": "ddc47d4e-67e4-41ad-85d9-388f86db5e05",
                "tabType": "tabgroup"
            }
        ]
    }
