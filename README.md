# CCRESPONSE-CRM
## API endpoints
### 1. Cases list
#### URL path - /api/cases
#### Query parameters:  
- Search.   
Use `search` keyword.  
Current search fields: `['customer_name', 'title'']`  
Example:
```
/cases?search=<value>
``` 

- Sort. 
You can sort by all non FM/M2M Case fields including FK/M2M ids as <FK field>_id and by 'customer__name', 'customer__phone_number'.  
Use `orderby_<field>` keyword to specify sort field and value to specify order destination (-1=descending, 1=ascending). Example:
```
/cases?orderby_created_at=1
```

- Filter.  
Use `<field>` keyword.  
You can filter by all non FM/M2M Case fields and by 'customer__name', 'customer__phone_number'.  
You should specify dates [in ISO format ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString).   
For date range you can specify `<datefield>__gte=<date start>`, `<datefield>__lt=<date end>`.  
Use `customer__phone_number=<phone number>` to filter by customer phone number.  
External party consist of introducers, solicitors and insurers. Use `exernal_parties=<id>` to filter results.  
If you want to filter cases by status (ongoing, payment_pack, settled), use `status=<status>`:
```
/api/cases?status=ongoing
/api/cases?status=ongoing,settled
```
**Fields that don't exist in Case will be ignored!**  
To specify values list just use `','`(comma) separator. Examples:
```
/cases?customer_id=1
/cases?customer_id=1,2,3
/cases?customer__phone_number=12345
/cases?customer__phone_number=12345,67890
/cases?external_parties=1
/cases?external_parties=1,2,3
/cases?created_at__gte=2021-02-19T08:50:09.784Z&created_at__lte=2021-03-19T08:50:09.784Z
```

- Pagination  
Use `page-size` to specify custom page size (50 entries by default) and `page` 
(1 by default) to specify page you're looking for.  
You will get response in the form
```
{
    "count": <all entries number>,
    "page-size": <page size>,
    "page": <current page number>
    "current": <current page url>
    "start": <start page url>,
    "end": <end page url>,
    "next": <next page url if exists else null>,
    "previous": <previous page url if exists else null>,
    "results": [{...},...]
}
```

#### Request examples (TODO: Replace with requests containing data in results)
In examples specified below authentication is disabled, 
so we don't provide any token. But if you want to resend 
these requests by your own, you should get token first and
insert header `'Authorization': 'Bearer <your token>'`

#### 1.
Request
```shell
curl http://localhost:8000/api/cases/
```
Response
```json
{
    "count":1,
    "page":1,
    "page_size":50,
    "current":"http://localhost:8000/api/cases/?page=1",
    "start":"http://localhost:8000/api/cases/?page=1",
    "end":"http://localhost:8000/api/cases/?page=1",
    "next":null,
    "previous":null,
    "results":[{
            "id": 34,
            "created_at": "2021-03-19T14:13:59.441922Z",
            "date_of_accident": "2021-03-19",
            "status": "settled",
            "customer": {
                "name": "abdm",
                "phone_number": ""
            },
            "external_parties": {
                "introducers": [],
                "solicitors": []
            },
            "injuries": [
                {
                    "id": 1,
                    "solicitor": 494845,
                    "date": "2021-04-16",
                    "status": "need_to_hotkey",
                    "type": "rta"
                },
                {
                    "id": 2,
                    "solicitor": 494845,
                    "date": "2020-05-19",
                    "status": "need_to_hotkey",
                    "type": "rta"
                }
            ],
            "case_notes": [],
            "tp_insurer_name": null
        }]
}
```

#### 2.
Request
```shell
curl http://localhost:8000/api/cases/\?customer_id\=1,2,3\&customer__phone_number\=012345,543210\&external_parties\=1,2,3\&created_at__gte\=2021-02-19T08:50:09.784Z\&orderby_created_at\=-1\&search\=asdasd
```
Response
```json
{
    "count":0,
    "page":1,
    "page_size":50,
    "current":"http://localhost:8000/api/cases/?customer_id=1,2,3&customer__phone_number=012345,543210&external_parties=1,2,3&created_at__gte=2021-02-19T08:50:09.784Z&orderby_created_at=-1&search=asdasd&page=1",
    "start":"http://localhost:8000/api/cases/?customer_id=1,2,3&customer__phone_number=012345,543210&external_parties=1,2,3&created_at__gte=2021-02-19T08:50:09.784Z&orderby_created_at=-1&search=asdasd&page=1",
    "end":"http://localhost:8000/api/cases/?customer_id=1,2,3&customer__phone_number=012345,543210&external_parties=1,2,3&created_at__gte=2021-02-19T08:50:09.784Z&orderby_created_at=-1&search=asdasd&page=1",
    "next":null,
    "previous":null,
    "results":[]
}
```

#### URL path - /api/cases/filtering-data/
__Example:__  
Request
```shell
curl http://localhost:8000/api/cases/filtering-data/
```
Response
```json
{
  "case": {
    "status": ["ongoing", "payment_pack", "settled"]
  },
  "customers": [
    {
      "id": 9,
      "name": "Martin Peate",
      "phone_number": "0796199490"
    }
  ],
  "external_parties": {
    "introducers": [
      {
        "id": 34,
        "name": "Jake Kelly"
      },
      {
        "id": 35,
        "name": "Jonh Smith"
      }
    ]
  },
   "solicitors": [
     {
       "id": 33,
       "name": "William Metcalfe"
     }
   ]
}
```


### 2. Case creation data
#### URL path - /api/cases/case-creation-data/
#### 1. Request

```shell
curl http://localhost:8000/api/cases/case-creation-data/
```

#### 2. Response
```json
{
  "external_parties": {
    "roles": [
      "insurer",
      "solicitor",
      "introducer"
    ],
    "insurers": [
      {
        "id": 24,
        "name": "Susan Bing",
        "ref": "insurer_ref",
        "phone_number": "12340987739",
        "email": "susanbing@gmail.com"
      }
    ],
    "introducers": [{
        "id": 13,
        "name": "Sirena Piterson",
        "ref": "ref_123"
      },
      {
        "id": 14,
        "name": "Dorata Parker",
        "ref": "ref_456"
      }],
    "solicitors": [
      {
        "id": 5,
        "name": "Mike Ross",
        "ref": "ref_1234"
      },
      {
        "id": 9,
        "name": "Harvey Specter",
        "ref": "ref_9409"
      }
      
    ]
  },
  "case": {
     "status": {
        "ongoing": "Ongoing",
        "payment_pack": "Payment Pack",
        "settled": "Settled",
        "rejected": "Rejected"
    },
   "circumstances": {
      "tired": "Tired",
      "sleepy": "Sleepy",
      "rainy": "Rainy"
    },
    "payment_status": {
      "paid": "Paid",
      "unpaid": "Unpaid",
      "waiting": "Waiting"
    }
  },
  "third_party": {
    "insurers": [
      {
        "id": 3,
        "name": "Tommy Bloom",
        "phone_number": "2334543232",
        "email": null,
        "ref": ""
      },
      {
        "id": 7,
        "name": "Kira Smith",
        "phone_number": "2323454232",
        "email": null,
        "ref": ""
      }
    ]
  },
  "injuries": {
    "statuses": [
        [
            "need_to_hotkey",
            "Need to hotkey"
        ],
        [
            "hotkeyed",
            "Hotkeyed"
        ],
        [
            "paid_also",
            "Paid Also"
        ]
    ],
    "types": [
        [
            "rta",
            "RTA"
        ],
        [
            "trip_slip",
            "Trip Slip"
        ],
        [
            "aaw",
            "AAW"
        ]
    ] 
  }
}
```


### 3. Case creation
#### URL path - /api/cases/

#### 1. Request
The third party insurer and related_external_parties can accept either the
ID of an existing objects or data to create a new one.

Example of data to create a new third party insurer:
```
{ 
  ...
  "third_party": {
    "insurer": {
      "name": "Sara Miller",
      "phone_number": "58302747602",
      "email": "saramiller2019@example.com",
      "ref": "some_ref"
    },
  ...
}
``` 

Set the existing third party insurer:
```
{
  ...
  "third_party": {
  "insurer":{
      "id": 34
  },
  ...
}
```

Create new external party:
```
 ...
 "related_external_parties": [
    {
      "name": "Monika Geller",
      "role": "insurer",
      "email": "monikageller@gmail.com",
      "ref": "some_insurer_ref",
      "phone_number": "12345678901"
    }
]
...
```

Set the existing external parties:
```
...
"related_external_parties": [
    {"id": 34}, 
    {"id": 23}
]
...
```

If you want to create injury/ies while creating the case you
should just specify it in an array, i.e:
```
"injuries": [
  {
    "solicitor": 494845,
    "date": "2021-04-16",
    "status": "need_to_hotkey",
    "type": "rta"
  }
],
```
To get list of injuries statuses/types available refer to 20.4, 20.5. Also 
available types/statuses can be found in 2. Case creation data

Request example:

```shell
curl -X POST -H "Content-Type: application/json" -d '{
  "instruction_date":"2021-02-25",
  "date_of_accident":"2021-02-25",
  "time_of_accident":"10:10",
  "location":"Bulevar Nikole Tesle 209, Novi Beograd",
  "circumstances": "tired",
  "other_info":"Side-Impact Collision",
  "weather":"Sunny weather",
  "status":"ongoing",
  "date_retained":"2021-02-25",
  "payment_status":"paid",
  "ack_comms":true,
  "customer":{
    "name":"William Metcalfe",
    "phone_number":"16329608993",
    "email":"williamm2019@gmail.com",
    "date_of_birth":"1990-02-25",
    "address":"134 Victoria Avenue, Manchester",
    "license_number":"MORGA7531116SM9IJ",
    "ni_number":"MQQ123456C",
    "notes":"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
  },
  "third_party":{
    "vehicle":{
      "vrn":"HU55 SMR",
      "make":"Kia",
      "model": "Rio",
      "mot_due":"2021-04-25",
      "tax_due":"2021-04-25",
      "daily_hire_rate": 20.34
    },
    "insurer":{
      "name":"Sara Miller",
      "phone_number":"58302747602",
      "email":"saramiller2019@example.com",
      "ref":"string"
    },
    "name":"Don Draper",
    "email":"dondraper@example.com",
    "phone_number":"01632960899",
    "notes":"Ultricies tristique nulla aliquet enim tortor at auctor.",
    "is_active":true,
    "policy_number":"123456789123",
    "address":"10 Downing Street, London"
  },
  "communication":"WhatsApp",
  "related_external_parties":[
    {
      "name":"Monika Geller",
      "role":"insurer",
      "email":"monikageller@gmail.com",
      "ref":"some_insurer_ref",
      "phone_number":"12345678901"
    },
    {
      "name":"Rachel Green",
      "role":"introducer",
      "introducer_fee":"350"
    },
    {
      "name":"Betty Skott",
      "role":"solicitor",
      "ref":"some_solicitor_ref"
    },
    {
      "id":23
    }
  ],
  "injuries": [
      {
        "solicitor": 494845,
        "date": "2021-04-16",
        "status": "need_to_hotkey",
        "type": "rta"
      }
  ],
  "customer_vehicle":{
    "vrn":"CR05 TON",
    "make":"Ford",
    "model": "Mondeo",
    "mot_due":"2021-06-25",
    "tax_due":"2021-06-25"
  }
}' http://localhost:8000/api/cases/
```

#### 2. Response  
A successful response has the status "201, Created" and an empty body with an additional "Location" header,
which specifies the location of the created object.
```
Location: /api/cases/{id}/details/
```

If the request contains errors, the status code will be "400, Bad Request". 

Example of an error messages when a request fails:
```json
{
 "third_party": {
    "name": [
      "party with this name already exists."
    ]
  },
  "time_of_accident": [
    "Time has wrong format. Use one of these formats instead: hh:mm[:ss[.uuuuuu]]."
  ]
}
```
If the error is not related to a specific field, the message will be:
```json
{
  "non_field_errors": [
    "the uniqueness of the names is not respected."
  ]
}
```


### 4. Case details
#### URL path - /api/cases/{pk}/details/

#### 1. Request example
```shell
curl -X GET "http://localhost:8000/api/cases/1/details/"
```

#### 2. Response
```json
{
    "id": 1,
    "instruction_date": "2021-02-25",
    "date_of_accident": "2021-02-25",
    "time_of_accident": "10:10:00",
    "location": "Bulevar Nikole Tesle 209, Novi Beograd",
    "circumstances": "tired",
    "other_info": "Side-Impact Collision",
    "weather": "Sunny weather",
    "status": "ongoing",
    "date_retained": "2021-02-25",
    "payment_status": "paid",
    "follow_up_date": "2021-03-22",
    "ack_comms": true,
    "customer": {
        "id": 1,
        "name": "William Metcalfe",
        "phone_number": "16329608993",
        "email": "williamm2019@gmail.com",
        "date_of_birth": "1990-02-25",
        "address": "134 Victoria Avenue, Manchester",
        "license_number": "MORGA7531116SM9IJ",
        "ni_number": "MQQ123456C",
        "notes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    },
    "third_party": {
        "id": 3,
        "vehicle": {
            "id": 2,
            "url": "http://127.0.0.1:8000/api/vehicles/2/",
            "vrn": "HU55 SMR",
            "make": "Kia",
            "model": "Rio",
            "mot_due": "2021-04-25",
            "tax_due": "2021-04-25"
        },
        "insurer": {
            "id": 2,
            "name": "Sara Miller",
            "phone_number": "58302747602",
            "email": "saramiller2019@example.com",
            "ref": "string"
        },
        "name": "Don Draper",
        "email": "dondraper@example.com",
        "phone_number": "01632960899",
        "created_at": "2021-02-28T15:05:56.810891Z",
        "updated_at": "2021-02-28T15:05:56.810941Z",
        "notes": "Ultricies tristique nulla aliquet enim tortor at auctor.",
        "is_active": true,
        "policy_number": "123456789123",
        "address": "10 Downing Street, London"
    },
    "communication": "WhatsApp",
    "related_external_parties": [
        {
            "id": 4,
            "name": "Monika Geller",
            "role": "insurer",
            "email": "monikageller@gmail.com",
            "ref": "some_insurer_ref",
            "phone_number": "12345678901",
            "introducer_fee": null
        },
        {
            "id": 5,
            "name": "Rachel Green",
            "role": "introducer",
            "email": null,
            "ref": "",
            "phone_number": "",
            "introducer_fee": "350.00"
        },
        {
            "id": 6,
            "name": "Betty Skott",
            "role": "solicitor",
            "email": null,
            "ref": "some_solicitor_ref",
            "phone_number": "",
            "introducer_fee": null
        },
        {
            "id": 23,
            "name": "Kate",
            "role": "introducer",
            "email": "kate@gmail.com",
            "ref": "",
            "phone_number": "+375 (33) 657 08 12",
            "introducer_fee": "430.00"
        }
    ],
    "injuries": [
        {
            "id": 3,
            "solicitor": 494845,
            "date": "2021-04-16",
            "status": "need_to_hotkey",
            "type": "rta"
        }
    ],
    "customer_vehicle": {
        "id": 1,
        "url": "http://127.0.0.1:8000/api/vehicles/1/",
        "vrn": "CR05 TON",
        "make": "Ford",
        "model": "Mondeo",
        "mot_due": "2021-06-25",
        "tax_due": "2021-06-25"
    },
    "has_bookings": false,
    "should_show_hire_sr": true
}
```

If you want to update case send PUT or PATCH request to this endpoint. For example if
you want to set should_show_hire_sr to true (which if false by default) you can send PATCH
request with the following body:
```json
{
  "should_show_hire_sr": true
}
```

### 5. Case Financials details
#### URL path - /api/cases/<case_id>/financials/
#### HTTP method - GET
Using this endpoint you can get case financials data. See examples below.  
__Example 1__:  
Request:
```shell
curl http://localhost:8000/api/cases/4/financials/
```
Response:
```json
{
    "invoices": [],
    "total_net": null,
    "total_vat": null,
    "total": null,
    "global_settled": null
}
```
__Example 2__:  
Request:
```shell
curl http://localhost:8000/api/cases/2/financials/
```
Response:
```json
{
    "invoices": [
        {
            "id": 2,
            "invoice_number": "asdfasdfsfdsaa",
            "invoice_date": "2021-03-29",
            "date_paid": null,
            "invoice_type": "hire",
            "settlement_status": "unsettled",
            "total_net": "88.10",
            "total_vat": "13.21",
            "settled_amount_net": "123.45",
            "settled_amount_vat": "0.12",
            "settled_amount_total": "110.32",
            "total": "101.31"
        },
        {
            "id": 4,
            "invoice_number": "asdasdasda",
            "invoice_date": "2021-03-29",
            "date_paid": null,
            "invoice_type": "storage_recovery",
            "settlement_status": "unsettled",
            "total_net": "4050.10",
            "total_vat": "607.51",
            "settled_amount_net": "105.21",
            "settled_amount_vat": "15.78",
            "settled_amount_total": "120.99",
            "total": "4657.61"
        }
    ],
    "total_net": "4138.20",
    "total_vat": "620.72",
    "total": "4758.92",
    "global_settled": "231.31"
}
```

### 6. Case Note creation
#### URL path - /api/cases/{pk}/notes/

#### 1. Request example
```shell
curl -X POST -H "Content-Type: application/json" -d '{"note": "Lorem ipsum"}' "http://localhost:8000/api/cases/1/notes/"  -H "Content-Type: application/json"
```

#### 2. Response
A successful response has the status "201, Created", and data about the created note.
```json
{
  "id": 7,
  "created_at": "2021-02-28T16:39:45.981341Z",
  "worker": "Jake Kelly",
  "note": "Lorem ipsum"
}
```

If the request contains errors, the status code will be "400, Bad Request".  
Example of message when a request fails:
```json
{
  "note": [
    "This field may not be blank."
  ]
}
```


### 7. Case Notes
#### URL path - /api/cases/{pk}/notes/

#### 1. Request example
```shell
curl -X GET "http://localhost:8000/api/cases/1/notes/"
```

#### 2. Response example
```json
[
  {
    "id": 1,
    "created_at": "2021-02-28T11:38:17.146301Z",
    "worker": "Jake Kelly",
    "note": "Lorem ipsum dolor sit amet."
  },
  {
    "id": 2,
    "created_at": "2021-02-28T12:37:07.592473Z",
    "worker": "Jake Kelly",
    "note": " Excepteur sint occaecat cupidatat non proident."
  }
]
```


### 8. Communications
#### URL path - /api/cases/{pk}/communications/

#### 1. Request example
```shell
curl -X GET "http://localhost:8000/api/cases/1/communications/"
```

#### 2. Response
```json
[
    {
        "id": 1,
        "worker": "Jake Kelly",
        "party": "Betty Skott",
        "type": "whats_app",
        "chat_messages": [
            {
                "id": 1,
                "subject": "",
                "message": "Ut enim ad minim veniam, quis nostrud exercitation.",
                "attachments": [],
                "received_at": "2021-02-28T10:49:15Z",
                "is_read": true,
                "sender": "Jake Kelly"
            },
            {
                "id": 3,
                "subject": "",
                "message": "Duis aute irure dolor in reprehenderit in voluptate",
                "attachments": [],
                "received_at": "2021-02-28T11:23:35Z",
                "is_read": false,
                "sender": "Betty Skott"
            }
        ]
    }
]
```

### 9. Invoices
#### I. Change invoice settled amount
#### URL path - /api/invoices/<invoice_id>/change-settled-amount/
#### HTTP method - POST
Using this endpoint you can change invoice settled amount.  
3 options can be specified: `settled_amount_net`, `settled_amount_vat`, `settled_amount_total`.  
`settled_amount_net` is required, 2 other are optional. If you don't specify any of
optional fields, it will be calculated automatically (vat = 20%).  
Values can be specified either as number or string

__Example 1__:   
Request:
```shell
curl -X POST -H 'Content-Type: application/json' -d '{"settled_amount_net": 123.45}' http://localhost:8000/api/invoices/2/change-settled-amount/
```
Response:
```json
{
    "id": 2,
    "invoice_number": "asdfasdfsfdsaa",
    "invoice_date": "2021-03-29",
    "date_paid": null,
    "invoice_type": "hire",
    "settlement_status": "unsettled",
    "total_net": "88.10",
    "total_vat": "13.21",
    "settled_amount_net": "123.45",
    "settled_amount_vat": "24.69",
    "settled_amount_total": "148.14",
    "total": "101.31"
}
```
__Example 2__:   
Request:
```shell
curl -X POST -H 'Content-Type: application/json' -d '{"settled_amount_net": "123.45", "settled_amount_vat": "0.12", "settled_amount_total": "110.32"}' http://localhost:8000/api/invoices/2/change-settled-amount/
```
Response:
```json
{
    "id": 2,
    "invoice_number": "asdfasdfsfdsaa",
    "invoice_date": "2021-03-29",
    "date_paid": null,
    "invoice_type": "hire",
    "settlement_status": "unsettled",
    "total_net": "88.10",
    "total_vat": "13.21",
    "settled_amount_net": "123.45",
    "settled_amount_vat": "0.12",
    "settled_amount_total": "110.32",
    "total": "101.31"
}
```



### 10. Dashboard
#### URL path - /api/dashboard/

#### 1. Request example
```shell
curl -X GET "http://localhost:8000/api/dashboard/"
```

#### 2. Response structure
Сomms notifications and diagram have no data yet, so they will be temporarily filled with empty values.
```json
{
    "general": {
        "total_due_in": 20565.65,
        "total_outstanding": 44565.65,
        "payment_pack_stage_amount": 100565.65,
        "total_daily_incurring": 1500.65,
        "cars_on_hire": 14,
        "total_cars": 30,
        "total_pi": 103,
        "ongoing_files": 480,
        "payment_pack_stage_count": 7
    },
    "scheduled_to_chase": [
        {
            "id": 1,
            "customer_name": "Courtney Henry",
            "doa": "2021-03-10",
            "follow_up_setter_name": "Jake Kelly",
            "is_overdue": true,
            "note": "Excepteur sint occaecat cupidatat non proident."
        },
        {
            "id": 2,
            "customer_name": "Jerome Bell",
            "doa": "2021-03-10",
            "follow_up_setter_name": "Jake Kelly",
            "is_overdue": false,
            "note": "Duis aute irure dolor in reprehenderit in voluptate."
        }
    ],
    "comms_notifications": [
        {
            "id": null,
            "subject": null,
            "sender_name": null,
            "message": null,
            "attachments": [],
            "received_at": null,
            "chat_type": null,
            "ref": null
        }
    ],
   "diagram": {
       "company": null,
       "google": null,
       "introducer": null
    }
}
```

### 11. Vehicle creation
#### URL path - /api/vehicles/
#### HTTP method - POST

#### 1. Request
Note: vrn - is vehicle registration number.    
The only required fields is 'daily_hire_rate'
Example of request body:
```json
{
  "vrn": "F4ABX",
  "make": "BMW",
  "model": "BMW 520D M Sport Auto (Blue)",
  "mot_due": "2017-03-10",
  "tax_due": "2018-01-01",
  "service_due": "2017-10-15",
  "date_purchased": "2018-03-12",
  "price_purchased": 43210.25,
  "tax_cost": 24,
  "mot_cost": 98.50,
  "notes": "Excepteur sint occaecat cupidatat non proident",
  "daily_hire_rate": "25.02",
  "daily_storage_rate": "25.00" 
}
```

#### 2. Response
A successful response has the status "201, Created" and an empty body with an additional "Location" header,
which specifies the location of the created object.
```
Location: /api/vehicles/{id}/
```
If the request contains errors, the status code will be "400, Bad Request".  
Example of an error message when a request fails:
```json
{
    "non_field_errors": [
        "at least one field must be provided."
    ]
}
```

### 12. Vehicles List
#### URL path - /api/vehicles/
#### HTTP method - GET

#### Query parameters:  
- Search.  
Use `search` keyword.  
(For now system searches only by 'customer_vehicle_cases__customer__name' field.)  
Example:
```
/vehicles?search=<value>
``` 

- Sort. 
You can sort by all non FM/M2M Vehicle fields including FK/M2M ids as <FK field>_id.  
Use `orderby_<field>` keyword to specify sort field and value to specify order destination (-1=descending, 1=ascending). Example:
```
/vehicles?orderby_created_at=1
```

- Filter.  
Use `<field>` keyword.  
You can filter by all non FM/M2M Vehicle fields including FK/M2M ids as <FK field>_id..  
You should specify dates [in ISO format ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString).   
For date range you can specify `<datefield>__gte=<date start>`, `<datefield>__lt=<date end>`.
To specify values list just use `','`(comma) separator. Examples:
```
/vehicles?id=1
/vehicles?id=1,2,3
```

- Pagination  
Use `page-size` to specify custom page size (50 entries by default) and `page` 
(1 by default) to specify page you're looking for.  
You will get response in the form
```
{
    "count": <all entries number>,
    "page-size": <page size>,
    "page": <current page number>
    "current": <current page url>
    "start": <start page url>,
    "end": <end page url>,
    "next": <next page url if exists else null>,
    "previous": <previous page url if exists else null>,
    "results": [{...},...]
}
```

#### Request examples
In examples specified below authentication is disabled, 
so we don't provide any token. But if you want to resend 
these requests by your own, you should get token first and then 
insert header `'Authorization': 'Bearer <your token>'`

#### 1.
Request
```shell
curl http://localhost:8000/api/vehicles/?page-size=3
```
Response
```json
{
    "count": 966011,
    "page": 1,
    "page_size": 3,
    "current": "http://localhost:8000/api/vehicles/?page-size=3&page=1",
    "start": "http://localhost:8000/api/vehicles/?page-size=3&page=1",
    "end": "http://localhost:8000/api/vehicles/?page-size=3&page=322004",
    "next": "http://localhost:8000/api/vehicles/?page-size=3&page=2",
    "previous": null,
    "additional_counts": {
        "booked": 1,
        "available": 966010
    },
    "results": [
        {
            "id": 5,
            "created_at": "2021-03-11T18:09:27.497315Z",
            "make": "",
            "model": "",
            "date_purchased": null,
            "mot_due": null,
            "tax_due": null,
            "service_due": null,
            "client_name": "abcde"
        },
        {
            "id": 6,
            "created_at": "2021-03-11T18:09:27.508199Z",
            "make": "",
            "model": "",
            "date_purchased": null,
            "mot_due": null,
            "tax_due": null,
            "service_due": null,
            "client_name": "abcdf"
        },
        {
            "id": 7,
            "created_at": "2021-03-11T18:09:27.518545Z",
            "make": "",
            "model": "",
            "date_purchased": null,
            "mot_due": null,
            "tax_due": null,
            "service_due": null,
            "client_name": "abcdg"
        }
    ]
}
```

#### 2.
Request
```shell
curl http://localhost:8000/api/vehicles?search=asd&page-size=3
```
Response
```json
{
    "count": 594,
    "page": 1,
    "page_size": 3,
    "current": "http://localhost:8000/api/vehicles/?search=asd&page-size=3&page=1",
    "start": "http://localhost:8000/api/vehicles/?search=asd&page-size=3&page=1",
    "end": "http://localhost:8000/api/vehicles/?search=asd&page-size=3&page=198",
    "next": "http://localhost:8000/api/vehicles/?search=asd&page-size=3&page=2",
    "previous": null,
    "additional_counts": {
        "booked": 0,
        "available": 594
    },
    "results": [
        {
            "id": 207465,
            "created_at": "2021-03-11T18:43:15.687261Z",
            "make": "",
            "model": "",
            "date_purchased": null,
            "mot_due": null,
            "tax_due": null,
            "service_due": null,
            "client_name": "asdbc"
        },
        {
            "id": 207466,
            "created_at": "2021-03-11T18:43:15.698939Z",
            "make": "",
            "model": "",
            "date_purchased": null,
            "mot_due": null,
            "tax_due": null,
            "service_due": null,
            "client_name": "asdbe"
        },
        {
            "id": 207467,
            "created_at": "2021-03-11T18:43:15.710747Z",
            "make": "",
            "model": "",
            "date_purchased": null,
            "mot_due": null,
            "tax_due": null,
            "service_due": null,
            "client_name": "asdbf"
        }
    ]
}
```

### 13. Vehicle get, update, delete
#### URL path - /api/vehicles/<id>
#### HTTP method - GET, PUT/PATCH, DELETE respectively

Fields for update are the same as for Vehicle create. 
__You can see those fields above__ ⬆

__Example (GET):__  
Request:
```shell
curl http://localhost:8000/api/vehicles/358801/
``` 
Response:
```json
{
    "id": 358801,
    "vrn": "0123456",
    "make": "abcdefg",
    "model": "abcdefh",
    "service_due": "2021-03-19",
    "date_purchased": "2021-03-19",
    "price_purchased": "0.20",
    "tax_cost": "0.10",
    "tax_due": "2021-03-19",
    "mot_due": "2021-03-19",
    "mot_cost": "0.20",
    "notes": "asdasdasdasdad",
    "daily_hire_rate": "25.02",
    "daily_storage_rate": "25.00"
}
```


### 14. ScheduledToChaseCase

__About ScheduledToChaseCase__:
It would be staff that are setting these chase dates. 
So when we send our initial report over to the insurer with 
our allegations of what has happened it can then take maybe 7 
days before that actually gets picked up and they respond to us. 
So we would set a chase/follow up for 8 days time on that file. 
In 8 days time the follow up task will appear in “schedule to chase” box. 
Once we have gone into the file and taken the chase action and set a new 
follow up date this would then be removed from the “schedule to chase” 
box on the dashboard. Also, if ay for example we do not chase the file 
on the day the reminder appears, the reminder will stay in the “schedule to chase” 
box the next day and remain at the top of the list highlighted red so we 
know its overdue. The follow ups will be listed in order of urgency/due date. 
These follow ups will be set within the client file somewhere.

#### How to set ScheduledToChaseCase time
Send POST request to `/api/cases/<case_id>/set-chase-date/`
with 'chase_date' parameter in the request body. 'chase_date' should be in any standard
format, i.e. format used by JSON.stringify().  
__Example__:
Request:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"chase_date": "Mon Mar 22 2021"}' http://localhost:8000/api/cases/4/set-chase-date/
```
Response:
```json
{"id":2,"case":4,"chase_date":"2021-03-22","is_overdued":true}
```

#### How to get list of ScheduledToChaseCase
Performance optimized and extended data about ScheduledToChaseCases can
be found in 'scheduled_cases' field of Dashboard data. You can relate to 9. Dashboard 
to get more information about it.
Meanwhile, you can get ScheduledToChaseCase objects data from 
`/api/cases/scheduled-to-chase/`  
__Example__:
Request:
```shell
curl http://localhost:8000/api/cases/scheduled-to-chase/
```
Response:
```json
[{"id":2,"case":4,"chase_date":"2021-03-22","is_overdued":true}]
```
Using the same endpoint you can send POST request to `/api/cases/scheduled-to-chase/` 
to create ScheduledToChaseCase and GET, PUT, PATCH, DELETE to 
`/api/cases/scheduled-to-chase/<id>/` to update ScheduledToChaseCase.

#### How to get chase_date for case
Case detail endpoint will provide you 'follow_up_date'. You can relate to `5. Case details to get more info`

### 15. Case Hire S&R
#### URL path: `/api/cases/<case_id>/hire-sr/`
#### HTTP's methods: GET, PUT
__GET__:  
Get Case Hire S&R data.  
__Example__:  
Request:
```shell
curl http://localhost:8000/api/cases/2/hire-sr/
```
Response:
```json
{
    "hire_details": {
        "id": 2,
        "vehicle_name": "abcdegy abcdegz",
        "vehicle_id": 358833,
        "created_at": "2021-03-29T17:42:25.904463Z",
        "updated_at": "2021-04-06T13:52:11.834066Z",
        "start_date": "2021-03-08",
        "end_date": "2021-03-29",
        "notes": "",
        "is_active": true,
        "daily_hire_rate": "4.00",
        "start_hire_latitude": "",
        "start_hire_longitude": "",
        "end_hire_latitude": "",
        "end_hire_longitude": "",
        "outsourced": false,
        "clear_booking": false,
        "collection": false,
        "collection_cost": "50.00",
        "delivery": false,
        "delivery_cost": "50.00",
        "cwd_required": false,
        "cwd_per_day": "12.00",
        "add_driver": false,
        "driver_price": "5.00",
        "sat_nav": false,
        "sat_nav_price": "5.00",
        "auto": false,
        "auto_price": "5.00",
        "towbar": false,
        "towbar_price": "5.00",
        "bluetooth": false,
        "bluetooth_price": "5.00",
        "ns_drive_charge": "0.00",
        "case": 2,
        "vehicle": 358833,
        "customer": 136045
    },
    "hire_validation": {
        "id": 1,
        "engs_instructed_date": null,
        "inspection_date": null,
        "report_received_date": null,
        "send_to_tp_date": null,
        "repairable": true,
        "total_loss_cil": true,
        "settle_offer": false,
        "offer_accepted": false,
        "cheque_received": false,
        "liability_admitted": false,
        "vehicle_hire": 2
    },
    "storage_details": {
        "id": 1,
        "days_in_storage": -20,
        "created_at": "2021-03-29T18:04:20.767929Z",
        "updated_at": "2021-04-06T13:52:11.850500Z",
        "start_date": "2021-03-08",
        "end_date": "2021-03-29",
        "notes": "",
        "is_active": true,
        "daily_storage_rate": "25.00",
        "vehicle": 358833,
        "customer": 136045
    },
    "recovery_details": {
        "id": 1,
        "created_at": "2021-03-29T18:04:40.427214Z",
        "updated_at": "2021-04-06T13:52:11.858266Z",
        "start_date": "2021-03-09",
        "end_date": "2021-03-29",
        "notes": "",
        "is_active": true,
        "total_price": "3500.00",
        "recovery_type": null,
        "call_out_charge": null,
        "winching_time": null,
        "road_cleanup": false,
        "skates": false,
        "inherited_fees": null,
        "engineers_fee": null,
        "vehicle": 358833,
        "customer": 136045
    }
}
```

__PUT__:  
The body to update should have the same form as response of GET.  
The only field that won't be used in update is hire_details -> vehicle_name. 
Any other field except ids can be changed. If you change id field of any instance
('hire_details', 'recovery_details', ...), such instance won't be updated  
__Example__:  
Request:  
```shell
curl -X PUT -H "Content-Type: application/json" -d '{
    "hire_details": {
        "id": 2,
        "vehicle_id": 358833,
        "created_at": "2021-03-29T17:42:25.904463Z",
        "updated_at": "2021-04-06T13:35:39.633300Z",
        "start_date": "2021-03-08",
        "end_date": "2021-03-29",
        "notes": "",
        "is_active": true,
        "daily_hire_rate": "4.00",
        "start_hire_latitude": "",
        "start_hire_longitude": "",
        "end_hire_latitude": "",
        "end_hire_longitude": "",
        "outsourced": true,
        "clear_booking": true,
        "collection": true,
        "collection_cost": "50.00",
        "delivery": true,
        "delivery_cost": "50.00",
        "cwd_required": true,
        "cwd_per_day": "12.00",
        "add_driver": true,
        "driver_price": "5.00",
        "sat_nav": true,
        "sat_nav_price": "5.00",
        "auto": true,
        "auto_price": "5.00",
        "towbar": true,
        "towbar_price": "5.00",
        "bluetooth": true,
        "bluetooth_price": "5.00",
        "ns_drive_charge": "0.00",
        "case": 2,
        "customer": 136045
    },
    "hire_validation": {
        "id": 1,
        "engs_instructed_date": null,
        "inspection_date": null,
        "report_received_date": null,
        "send_to_tp_date": null,
        "repairable": true,
        "total_loss_cil": true,
        "settle_offer": false,
        "offer_accepted": false,
        "cheque_received": false,
        "liability_admitted": false,
        "vehicle_hire": 2
    },
    "storage_details": {
        "id": 1,
        "days_in_storage": -20,
        "created_at": "2021-03-29T18:04:20.767929Z",
        "updated_at": "2021-03-29T18:04:20.767948Z",
        "start_date": "2021-03-08",
        "end_date": "2021-03-29",
        "notes": "",
        "is_active": true,
        "daily_storage_rate": "25.00",
        "vehicle": 358833,
        "customer": 136045
    },
    "recovery_details": {
        "id": 1,
        "created_at": "2021-03-29T18:04:40.427214Z",
        "updated_at": "2021-03-29T18:04:40.427284Z",
        "start_date": "2021-03-09",
        "end_date": "2021-03-29",
        "notes": "",
        "is_active": true,
        "total_price": "3500.00",
        "recovery_type": null,
        "call_out_charge": null,
        "winching_time": null,
        "road_cleanup": false,
        "skates": false,
        "inherited_fees": null,
        "engineers_fee": null,
        "vehicle": 358833,
        "customer": 136045
    }
}' http://localhost:8000/api/cases/2/hire-sr/
```
Response:
```json
{
    "hire_details": {
        "id": 2,
        "vehicle_name": "abcdegy abcdegz",
        "vehicle_id": 358833,
        "created_at": "2021-03-29T17:42:25.904463Z",
        "updated_at": "2021-04-06T16:24:20.208578Z",
        "start_date": "2021-03-08",
        "end_date": "2021-03-29",
        "notes": "",
        "is_active": true,
        "daily_hire_rate": "4.00",
        "start_hire_latitude": "",
        "start_hire_longitude": "",
        "end_hire_latitude": "",
        "end_hire_longitude": "",
        "outsourced": true,
        "clear_booking": true,
        "collection": true,
        "collection_cost": "50.00",
        "delivery": true,
        "delivery_cost": "50.00",
        "cwd_required": true,
        "cwd_per_day": "12.00",
        "add_driver": true,
        "driver_price": "5.00",
        "sat_nav": true,
        "sat_nav_price": "5.00",
        "auto": true,
        "auto_price": "5.00",
        "towbar": true,
        "towbar_price": "5.00",
        "bluetooth": true,
        "bluetooth_price": "5.00",
        "ns_drive_charge": "0.00",
        "case": 2,
        "vehicle": 358833,
        "customer": 136045
    },
    "hire_validation": {
        "id": 1,
        "engs_instructed_date": null,
        "inspection_date": null,
        "report_received_date": null,
        "send_to_tp_date": null,
        "repairable": true,
        "total_loss_cil": true,
        "settle_offer": false,
        "offer_accepted": false,
        "cheque_received": false,
        "liability_admitted": false,
        "vehicle_hire": 2
    },
    "storage_details": {
        "id": 1,
        "days_in_storage": -20,
        "created_at": "2021-03-29T18:04:20.767929Z",
        "updated_at": "2021-04-06T16:24:20.223243Z",
        "start_date": "2021-03-08",
        "end_date": "2021-03-29",
        "notes": "",
        "is_active": true,
        "daily_storage_rate": "25.00",
        "vehicle": 358833,
        "customer": 136045
    },
    "recovery_details": {
        "id": 1,
        "created_at": "2021-03-29T18:04:40.427214Z",
        "updated_at": "2021-04-06T16:24:20.230327Z",
        "start_date": "2021-03-09",
        "end_date": "2021-03-29",
        "notes": "",
        "is_active": true,
        "total_price": "3500.00",
        "recovery_type": null,
        "call_out_charge": null,
        "winching_time": null,
        "road_cleanup": false,
        "skates": false,
        "inherited_fees": null,
        "engineers_fee": null,
        "vehicle": 358833,
        "customer": 136045
    }
}
```

### 16. Vehicle Hires
### Create, list
#### URL path: /vehicle-hires/
#### List: GET
To get list of vehicle bookings just send request to the specified URL.  
You can order hires list by "client_name" or "booking_range". To do so add 
'orderby_<field>=<1 | -1>' to your query parameters.  
To get hires of vehicle specify vehicle id in query parameters as in the following example:
start\end_date are specified in ISO format
Request:
```shell
curl http://localhost:8000/api/vehicle-hires/?vehicle_id=358833&orderby_booking_range=-1
```
Response:
```json
{
    "count": 5,
    "page": 1,
    "page_size": 50,
    "current": "http://localhost:8000/api/vehicle-hires/?vehicle_id=358833&orderby_start_date=-1&page=1",
    "start": "http://localhost:8000/api/vehicle-hires/?vehicle_id=358833&orderby_start_date=-1&page=1",
    "end": "http://localhost:8000/api/vehicle-hires/?vehicle_id=358833&orderby_start_date=-1&page=1",
    "next": null,
    "previous": null,
    "additional_counts": null,
    "results": [
        {
            "id": 4,
            "created_at": "2021-04-06T13:47:32.510483Z",
            "client_name": "abcd",
            "booking_range": "08/03/2021 - 29/03/2021",
            "start_date": "2021-03-08",
            "end_date": "2021-03-29"
        },
        {
            "id": 5,
            "created_at": "2021-04-06T13:48:43.399668Z",
            "client_name": "abcd",
            "booking_range": "08/03/2021 - 29/03/2021",
            "start_date": "2021-03-08",
            "end_date": "2021-03-29"
        },
        {
            "id": 6,
            "created_at": "2021-04-06T13:49:51.558139Z",
            "client_name": "abcd",
            "booking_range": "08/03/2021 - 29/03/2021",
            "start_date": "2021-03-08",
            "end_date": "2021-03-29"
        },
        {
            "id": 7,
            "created_at": "2021-04-06T13:50:23.351401Z",
            "client_name": "abcd",
            "booking_range": "08/03/2021 - 29/03/2021",
            "start_date": "2021-03-08",
            "end_date": "2021-03-29"
        },
        {
            "id": 2,
            "created_at": "2021-03-29T17:42:25.904463Z",
            "client_name": "abcd",
            "booking_range": "08/03/2021 - 29/03/2021",
            "start_date": "2021-03-08",
            "end_date": "2021-03-29"
        }
    ]
}
```

#### Create: POST
#### POST
Check the example below for get-put.
To set customer you can specify in "customer" data either name (not recommended) 
or id field with corresponding value. Case and invoice fields are not required.  
Other hire fields will be taken from dict and set directly
### Get, update, delete
#### URL path: /vehicle-hires/<pk>/
#### GET
Request:
```shell
curl http://localhost:8000/api/vehicle-hires/2/
```
Response:
```json
{
    "invoice": 2,
    "case": 4,
    "vehicle": 358833,
    "customer": {
        "id": 136045,
        "name": "abcd",
        "phone_number": "",
        "email": null,
        "date_of_birth": null,
        "address": "",
        "license_number": "",
        "ni_number": "",
        "notes": ""
    },
    "daily_hire_rate": "4.00",
    "start_hire_latitude": "",
    "start_hire_longitude": "",
    "end_hire_latitude": "",
    "end_hire_longitude": "",
    "start_date": "2021-03-08",
    "end_date": "2021-03-29",
    "notes": "",
    "created_at": "2021-03-29T17:42:25.904463Z"
}
```
#### PUT
To change `customer` you can specify in "customer" data either `name` (not recommended) 
or `id` field with corresponding value. Case and invoice fields are not required.  
Any other field can be changed by changing this object above and sending it back to backend

### 17. Case documents (ALL)

#### URL path: /cases/documents/, HTTP's methods: GET, POST
#### URL path: /cases/documents/<document_id>/, HTTP's methods: GET, POST, PUT, PATCH, DELETE

Sending GET request to /cases/documents/ you can get list of ALL documents. It supports 
pagination. More info about pagination you can find above.   
Using other path-method combinations you can execute CRUD actions on documents
`filename` and `username` fields are readonly.
User set on update or create is determined automatically

__Example__:  
Request:
```shell
curl http://localhost:8000/api/cases/documents/
```
Response:
```json
{
    "count": 2,
    "page": 1,
    "page_size": 50,
    "current": "http://localhost:8000/api/cases/documents/?page=1",
    "start": "http://localhost:8000/api/cases/documents/?page=1",
    "end": "http://localhost:8000/api/cases/documents/?page=1",
    "next": null,
    "previous": null,
    "additional_counts": null,
    "results": [
        {
            "user": 1,
            "case": 2,
            "filename": "Pipfile.lock",
            "file": "https://ccresponse-crm.s3.amazonaws.com/dev/media/private/case_documents/Pipfile.lock?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3FI52BKQQ6WSG5QU%2F20210408%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20210408T091854Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=19bd3397b83da9026c0b2874546ee9f497ec70a566985d6667f509c2f597d26e",
            "type": "TC",
            "description": "pipfile lock",
            "created_at": "08/04/2021 09:04:09",
            "username": "user123"
        },
        {
            "user": 1,
            "case": 33,
            "filename": "README.md",
            "file": "https://ccresponse-crm.s3.amazonaws.com/dev/media/private/case_documents/README.md?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3FI52BKQQ6WSG5QU%2F20210408%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20210408T091854Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=9aae8f1d073464550aa9f4b591f4640919c719cbcdc365d4d6ba86aaab37aed6",
            "type": "TB",
            "description": "readme",
            "created_at": "08/04/2021 09:16:10",
            "username": "user123"
        }
    ]
}
```

### 18. Case documents (Case related)
#### URL path: /cases/<case_id>/documents/
#### HTTP's methods: GET, POST

GET lists all case related documents same as in 18. Pagination is supported. 
POST creates a new document for the case found by case_id.
`filename` and `username` fields are readonly.
User set on update or create is determined automatically

__Example__:  
Request:
```shell
curl http://localhost:8000/api/cases/2/documents/
```
Response:
```json
{
    "count": 1,
    "page": 1,
    "page_size": 50,
    "current": "http://localhost:8000/api/cases/2/documents/?page=1",
    "start": "http://localhost:8000/api/cases/2/documents/?page=1",
    "end": "http://localhost:8000/api/cases/2/documents/?page=1",
    "next": null,
    "previous": null,
    "additional_counts": null,
    "results": [
        {
            "user": 1,
            "case": 2,
            "filename": "Pipfile.lock",
            "file": "https://ccresponse-crm.s3.amazonaws.com/dev/media/private/case_documents/Pipfile.lock?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3FI52BKQQ6WSG5QU%2F20210408%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20210408T091943Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=72f27d06aa3981feb1cdadd46731f25ad698501384374548e2cd8010e3f999b2",
            "type": "TC",
            "description": "pipfile lock",
            "created_at": "08/04/2021 09:04:09",
            "username": "user123"
        }
    ]
}
```

### 19. Vehicle Expenses
#### URL path: /expenses?vehicle_id=<vehicle_id>. HTTP's methods: GET, POST
GET supports pagination, and order by cost, date, description. To see how
to do it you can relate to _1. Cases list_  

__GET Example:__  
Request:
```shell
curl http://localhost:8000/api/expenses/?vehicle_id=1 
```
Response:
```json
{
    "count": 6,
    "page": 1,
    "page_size": 50,
    "current": "http://localhost:8000/api/expenses/?vehicle_id=1&page=1",
    "start": "http://localhost:8000/api/expenses/?vehicle_id=1&page=1",
    "end": "http://localhost:8000/api/expenses/?vehicle_id=1&page=1",
    "next": null,
    "previous": null,
    "grand_total": 21679.0,
    "results": [
        {
            "id": 1,
            "date": "01/04/2021",
            "description": "lllllll",
            "cost": "100.00",
            "vehicle": 1
        },
        {
            "id": 2,
            "date": "03/04/2021",
            "description": "wwwww",
            "cost": "1390.00",
            "vehicle": 1
        },
        {
            "id": 3,
            "date": "08/04/2021",
            "description": "llllllll",
            "cost": "100.00",
            "vehicle": 1
        },
        {
            "id": 4,
            "date": "02/04/2021",
            "description": "ssssss",
            "cost": "100.00",
            "vehicle": 1
        },
        {
            "id": 5,
            "date": "23/04/2021",
            "description": "new expence",
            "cost": "9990.00",
            "vehicle": 1
        },
        {
            "id": 6,
            "date": "22/04/2021",
            "description": "Second exoence",
            "cost": "9999.00",
            "vehicle": 1
        }
    ]
}
```
__POST Example:__  
Request:
```shell
curl -X POST -H "Content-Type: application/json" -d '{
  "date": "17/04/2021",
  "cost": "23.02",
  "description": "some expense2" 
}' http://localhost:8000/api/expenses/?vehicle_id=358801
```
Response:
```json
{
    "id": 2,
    "date": "17/04/2021",
    "description": "some expense2",
    "cost": "23.02"
}
```
#### URL path: /expenses/<expense_id>. HTTP's methods: GET, PUT, DELETE
__GET example:__  
Request:
```shell
curl http://localhost:8000/api/expenses/2/
```
Response:
```json
{
    "id": 2,
    "date": "17/04/2021",
    "description": "some expense2",
    "cost": "23.02"
}
```
__PUT example:__  
Request:
```shell
curl -X PUT -H "Content-Type: application/json" -d '{
  "date": "19/04/2021",
  "cost": "25.02",
  "description": "some expense2"
}' http://localhost:8000/api/expenses/2/
```
Response:
```json
{
    "id": 2,
    "date": "19/04/2021",
    "description": "some expense2",
    "cost": "25.02"
}
```

### 20. Injuries
#### 1) URL path: /cases/<case_id>/injury/. HTTP's methods: GET
Returns the latest (ordered by `created_at` not `date`) injury
registered for case. If no injuries found, it returns {} 
(empty object)

__Example - GET:__  
Request:
```shell
http://localhost:8000/api/cases/34/injury/
```
Response:
```json
{
    "id": 1,
    "case": 34,
    "solicitor": 494845,
    "date": "16/04/2021",
    "type": "rta",
    "status": "need_to_hotkey"
}
```
#### 2) URL path: /injuries/. HTTP's methods: GET, POST
GET - list (pagination supported), POST - create
On create, if solicitor (it is an instance of ExternalParty class) was specified,
but not found, 401 Bad Request will be returned with the following data:
```json
{
    "solicitor": [
        "Specified external party is not solicitor"
    ]
}
```

__Types allowed:__  
rta, trip_slip, aaw

__Statuses allowed:__  
need_to_hotkey, hotkeyed, paid_also

__Example - GET:__  
Request:
```shell
curl http://localhost:8000/api/injuries/ 
```
Response:
```json
{
    "count": 2,
    "page": 1,
    "page_size": 50,
    "current": "http://localhost:8000/api/injuries/?page=1",
    "start": "http://localhost:8000/api/injuries/?page=1",
    "end": "http://localhost:8000/api/injuries/?page=1",
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "case": 34,
            "solicitor": 494845,
            "date": "16/04/2021",
            "type": "rta",
            "status": "need_to_hotkey"
        },
        {
            "id": 2,
            "case": 34,
            "solicitor": 494845,
            "date": "20/04/2021",
            "type": "rta",
            "status": "need_to_hotkey"
        }
    ]
}
```
__Example - POST:__  
Request:
```shell
curl -X POST -H "Content-Type: application/json" -d '{
  "case": 34,
  "solicitor": 494845,
  "date": "20/04/2021",
  "type": "rta",
  "status": "need_to_hotkey"
}' http://localhost:8000/api/injuries/
```
Response:
```json
{
    "id": 2,
    "case": 34,
    "solicitor": 494845,
    "date": "20/04/2021",
    "type": "rta",
    "status": "need_to_hotkey"
}
```
#### 3) URL path: /injuries/<injury_id>/. HTTP's methods: GET, PUT, DELETE
__Example - GET:__  
Request:
```shell
curl http://localhost:8000/api/injuries/2/
```
Response:
```json
{
    "id": 2,
    "case": 34,
    "solicitor": 494845,
    "date": "20/04/2021",
    "type": "rta",
    "status": "need_to_hotkey"
}
```
__Example - POST:__  
Request:
```shell
curl -X PUT -H "Content-Type: application/json" -d '{
  "id": 2,
  "case": 34,
  "solicitor": 494845,
  "date": "19/05/2020",
  "type": "rta",
  "status": "need_to_hotkey"
}' http://localhost:8000/api/injuries/2/
```
Response:
```json
{
    "id": 2,
    "case": 34,
    "solicitor": 494845,
    "date": "19/05/2020",
    "type": "rta",
    "status": "need_to_hotkey"
}
```
#### 4) URL path: /injuries/statuses/, HTTP's method: GET
Returns available injuries statuses. First values is the database value, second - 
value to show on frontend page.  
__Example:__  
Request:
```shell
curl http://localhost:8000/api/injuries/statuses/
```
Response:
```json
[
    [
        "need_to_hotkey",
        "Need to hotkey"
    ],
    [
        "hotkeyed",
        "Hotkeyed"
    ],
    [
        "paid_also",
        "Paid Also"
    ]
]
```
#### 5) URL path: /injuries/types/, HTTP's method: GET
Returns available injuries types. First values is the database value, second - 
value to show on frontend page.  
__Example:__  
Request:
```shell
curl http://localhost:8000/api/injuries/types/
```
Response:
```json
[
    [
        "rta",
        "RTA"
    ],
    [
        "trip_slip",
        "Trip Slip"
    ],
    [
        "aaw",
        "AAW"
    ]
]
```

### 21. Document templates
#### 1) URL path: /cases/documents/templates/. HTTP's methods: GET
Returns data about the document templates. 
Request:
```shell
http://localhost:8000/api/cases/documents/templates/
```
Response:
```json

{
    "document_templates": [
        {
            "id": 1,
            "name": "Witness Statement"
        },
        {
            "id": 2,
            "name": "Release note - Motor Move Uk"
        },
        {
            "id": 3,
            "name": "Generate Payment Pack DRAFT"
        }
    ]
}
```

#### 2) URL path: /cases/<case_id>documents/generate-from-template/. HTTP's methods: POST
This endpoint generates document from a template and returns a "Content-Disposition" header,
that contains the attachment. Attachment will be loaded and saved locally.  
Request:
```shell
curl -X POST -H "Content-Type: application/json" -d '{
  "document_template_id": 1
}' http://localhost:8000/api/cases/1/documents/generate-from-template/
```
Response:
```shell
Content-Disposition: attachment; filename=Release Note - Mansfield Group.docx
```

### 22. Addresses
#### URL path: /addresses/. HTTP's methods: GET, POST
#### URL path: /addresses/<address_id>/. HTTP's methods: GET, PUT, PATCH, DELETE
Address contains only one field `address`. Address supports search. To use it just add 
`s=<search value>` to query parameters. 
__Example 1__:  
Request:
```shell
curl http://localhost:8000/api/addresses/
```
Response:
```json
[
    {
        "id": 7,
        "address": "Mirostr"
    },
    {
        "id": 8,
        "address": "Street"
    },
    {
        "id": 9,
        "address": "134 Victoria Avenue, Manchester"
    }
]
```
__Example 2__:  
Request:
```shell
curl http://localhost:8000/api/addresses/?s=134
```
Response:
```json
[
    {
        "id": 9,
        "address": "134 Victoria Avenue, Manchester"
    }
]
```

### 23. Contacts
#### 1) Insurers
##### 1.1) URL path: /contacts/insurers/. HTTP's methods: POST
With this endpoint you can create a new insurer.  
__Example:__  
Request:
```shell
curl -X POST -H "Content-Type: application/json" -d '{
        "name": "Some name",
        "email": "some.name@gmail.com",
        "phone_number": "1234567890",
        "is_active": true
    }' http://localhost:8000/api/contacts/insurers/
```
Response:  
A successful response has the status "201, Created" and body with data about created insurer.
```json
{
  "id": 2,
  "name": "Some name",
  "email": "some.name@gmail.com",
  "phone_number": "1234567890",
  "is_active": true
}
```
##### 1.2) URL path: /contacts/insurers/<insurer_id>/. HTTP's methods: GET, PUT, PATCH
GET - get data about insurer  
PUT and PATCH - update data about insurer  
__Example - GET:__  
Request:
```shell
curl http://localhost:8000/api/contacts/insurers/2/
```
Response:
```json
{
    "id": 2,
    "name": "Some name",
    "email": "some.email@gmail.com",
    "phone_number": "1234567890",
    "is_active": true
}
```
__Example - PUT or PATCH:__  
Request:
```shell
curl -X PUT -H "Content-Type: application/json" -d '{
  "name": "Some new name",
  "email": "some.new.email@gmail.com",
  "phone_number": "0987654321",
  "is_active": false
}' http://localhost:8000/api/contacts/injuries/2/
```
Response:
```json
{
    "id": 2,
    "name": "Some new name",
    "email": "some.new.email@gmail.com",
    "phone_number": "0987654321",
    "is_active": false
}
```

## Fast & Auxiliary endpoints:
### 1. Customers. Data for assign
#### URL path: /customers/data-for-assign/
#### HTTP's method: GET
To get data to use for client change you can use this endpoint 
that returns id and name of all customers and works very fast

__Example__:  
Request:
```shell
curl http://localhost:8000/api/customers/data-for-assign/
```
Response:
```json
[
    {
        "id": 136045,
        "name": "abcdjhgasdj"
    },
    {
        "id": 136046,
        "name": "sfkjdbfkjdsbkf"
    }
]
```

### 2. Solicitors. Data for assign
#### URL path: /solicitors/data-for-assign/
#### HTTP's method: GET
__Example:__  
Request:
```shell
http://localhost:8000/api/solicitors/data-for-assign/
```
Response:
```json
[
    {
        "id": 494845,
        "name": "BABAKAR"
    },
    {
        "id": 494847,
        "name": "ARAKAKAKAP"
    }
]
```

### 3. Vehicles. Data for assign
#### URL path: /vehicle/data-for-assign/
#### HTTP's method: GET
You can filter vehicles by owner. To do so, add `owner=<owner>` to query parameters.
Available owners are: `company`, `third_party`, `customer`

Also you can filter by status. To do so, add `status=<status>` to query parameters.
Available statuses are: `Booked`, `Available`, `Sold`

__Example:__  
Request:
```shell
http://localhost:8000/api/vehicles/data-for-assign/
```
Response:
```json
[
    {
        "id": 717601,
        "name": "Ford Mondeo CR05 TON"
    },
    {
        "id": 717602,
        "name": "Kia Rio HU55 SMR"
    }
]
```
