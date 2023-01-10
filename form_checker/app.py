from flask import Flask, request
from form_checker.form import check_fields_in_db, get_temp_by_fields
from form_checker.form import prepare_form
from form_checker.validator import validate


app = Flask(__name__)


@app.post('/get_form')
def form_post():
    data = request.json
    field_names_in_db = check_fields_in_db(data)

    if field_names_in_db is None:
        return prepare_form(data)

    template = get_temp_by_fields(field_names_in_db)
    validated_fields = validate(data, template)

    if validated_fields != field_names_in_db:
        template = get_temp_by_fields(validated_fields)

    if not template:
        return prepare_form(data)

    template_name = template.get('name')
    return {'FormName': template_name}
