from form_checker.db import get_field_names_in_db, find_template_in_db
from form_checker.validator import get_type


def check_fields_in_db(data_from_form) -> list | None:
    fields_names_from_form = list(data_from_form)

    field_names_in_db = get_field_names_in_db(fields_names_from_form)

    return field_names_in_db if field_names_in_db else None


def get_temp_by_fields(field_names: list) -> dict:
    if not field_names:
        return dict()
    found_template = find_template_in_db(field_names)
    return found_template


def prepare_form(data: dict) -> dict:
    result = dict()

    for field_name, field_value in data.items():
        result[field_name] = get_type(str(field_value))

    return result
