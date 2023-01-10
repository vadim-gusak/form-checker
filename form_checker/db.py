from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import find_dotenv, load_dotenv
from os import getenv


load_dotenv(find_dotenv())
DB_NAME = getenv('DB_NAME')
COLLECTION_NAME = getenv('COLLECTION_NAME')
DB_URL = getenv('MONGO_URL') + ':' + getenv('PORT')


def get_field_names_in_db(names: list) -> list:
    result = list()

    client = MongoClient(DB_URL)
    try:
        db = client[DB_NAME]
        forms_collection = db[COLLECTION_NAME]
        for name in names:
            number_of_forms = forms_collection.count_documents(
                {name: {"$exists": True}}
            )
            if number_of_forms > 0:
                result.append(name)

    except PyMongoError:
        return result
    finally:
        client.close()

    return result


def find_template_in_db(names: list) -> dict:
    templates = list()
    fields_to_check_in_db = {name: {"$exists": True} for name in names}

    client = MongoClient(DB_URL)
    try:
        db = client[DB_NAME]
        forms_collection = db[COLLECTION_NAME]
        found_templates_cursor = forms_collection.find(fields_to_check_in_db)

        for temp in found_templates_cursor:
            templates.append(temp)
    except PyMongoError:
        return dict()
    finally:
        client.close()

    min_len_of_temps = len(templates[0])
    result_template = templates[0]
    for temp in templates:
        if len(temp) < min_len_of_temps:
            min_len_of_temps = len(temp)
            result_template = temp

    return result_template
