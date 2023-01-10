from datetime import datetime
import re
from validators.email import email


def get_type(data: str) -> str:
    if is_date(data):
        return 'date'

    if is_phone(data):
        return 'phone'

    if is_email(data):
        return 'email'

    return 'text'


def is_date(data: str) -> bool:
    try:
        date = datetime.strptime(data, '%Y-%m-%d').date()
        if date:
            return True
    except ValueError as e:
        pass

    try:
        date = datetime.strptime(data, '%d.%m.%Y').date()
        if date:
            return True
    except ValueError as e:
        pass

    return False


def is_phone(data: str) -> bool:
    match = re.fullmatch(r'[+][7]\d{10}', data)
    return True if match else False


def is_email(data: str) -> bool:
    valid = email(data)
    return True if valid else None


def validate(data: dict, template: dict) -> list:
    result = list()

    for field_name, field_type in template.items():
        if field_name == '_id' or field_name == 'name':
            continue
        elif field_type == 'date' and is_date(data[field_name]):
            result.append(field_name)
        elif field_type == 'phone' and is_phone(data[field_name]):
            result.append(field_name)
        elif field_type == 'email' and is_email(data[field_name]):
            result.append(field_name)
        elif field_type == 'text':
            result.append(field_name)

    return result
