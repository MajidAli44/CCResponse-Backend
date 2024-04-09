from django.core.validators import RegexValidator

PHONE_NUMBER_REGEX = RegexValidator(
    regex=r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
    message='Only international format'
)

NI_NUMBER_REGEX = RegexValidator(
    regex=r'^\s*[a-zA-Z]{2}(?:\s*\d\s*){6}[a-zA-Z]?\s*$'
)
