[![Lint and Pytest](https://github.com/vadim-gusak/form-checker/actions/workflows/main.yml/badge.svg)](https://github.com/vadim-gusak/form-checker/actions/workflows/main.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/0033b8301644c32c7d35/maintainability)](https://codeclimate.com/github/vadim-gusak/form-checker/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0033b8301644c32c7d35/test_coverage)](https://codeclimate.com/github/vadim-gusak/form-checker/test_coverage)

# Web-приложение для определения заполненных форм

В этом репозитории находится мое решение [тестового задания.](task_description.md)

Использовал:
- Flask
- MongoDB
- Docker
- Poetry

[Используемые шаблоны форм.](db/forms.json)

## Запуск

Для сборки образа и запуска контейнеров воспользуйтесь командой:
```commandline
docker compose up -d
```
## Тесты

[Тесты](tests/test_app.py) можно запустить так:
```commandline
docker exec form-checker_container pytest
```
А можно подключиться к контейнеру. Для этого введите:
```commandline
docker exec -it form-checker_container sh
```
Запуск тестов после подключения:
```commandline
pytest
```
Вне контейнера также можно направить запросы к серверу:
```commandline
curl -X 'POST' \
  'localhost:5000/get_form' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'created_at=09.01.2023&user_email=test@mail.ru&unknown_field=test_text&user_phone=%2B79146789281'
```
И получить ответ:
```commandline
{"FormName":"AllFields"}
```
Ещё варианты:
```commandline
curl -X 'POST' \
  'localhost:5000/get_form' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'created_at=091.01.20232&wow=%2B79146789281&lol=12.12.2023&kek=dasdasd@mail.io&ololo=24234sdfsdf&user_phone=%2B79146789281'
```
```commandline
{"FormName":"OnlyPhone"}
```
Пример распознования "на лету":
```commandline
curl -X 'POST' \
  'localhost:5000/get_form' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'created_at=091.01.20232&wow=%2B79146789281&lol=12.12.2023&kek=dasdasd@mail.io&ololo=24234sdfsdf'
```
```commandline
{
  "created_at": "text",
  "kek": "email",
  "lol": "date",
  "ololo": "text",
  "wow": "phone"
}
```
