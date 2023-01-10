from form_checker.app import app


app.config.update(
    SECRET_KEY='test_secret',
    TESTING=True
)


def test_form_post():
    post_data = {
        'created_at': "09.01.2023",
        "user_email": "test@mail.ru",
        "unknown_field": "test_text",
        "user_phone": "+79146789281"
    }
    response = app.test_client().post(
        '/get_form',
        data=post_data,
        content_type='application/x-www-form-urlencoded'
    )

    assert response.json == {'FormName': 'AllFields'}


def test_form_post_one_field():
    post_data = {
        'created_at': "09.01.2023",
        "lol": "test@mail.ru",
        "kek": "test_text",
        "zzzz": "+79146789281"
    }
    response = app.test_client().post(
        '/get_form',
        data=post_data,
        content_type='application/x-www-form-urlencoded'
    )

    assert response.json == {'FormName': 'OnlyDate'}


def test_form_post_unknown_fields():
    post_data = {
        'blah': "09.01.2023",
        "lol": "test@mail.ru",
        "kek": "test_text",
        "zzzz": "+79146789281"
    }
    response = app.test_client().post(
        '/get_form',
        data=post_data,
        content_type='application/x-www-form-urlencoded'
    )

    assert response.json == {
        'blah': 'date', 'kek': 'text', 'lol': 'email', 'zzzz': 'phone'
    }
