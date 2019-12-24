from django.core.exceptions import ValidationError

def validate_email(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('Not valid email')
    return value

def zip_validator(value):
    if not value.startswith('AZ'):
        raise ValidationError('Not valid AZ zip ')
    return value
