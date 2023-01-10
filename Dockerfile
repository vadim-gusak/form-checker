FROM python:3.10.9-alpine3.17

ENV POETRY_VERSION=1.3.1

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY . .

RUN poetry install --no-interaction --no-ansi

CMD [ "poetry", "run", "flask", "--app", "form_checker:app", "run", "--host", "0.0.0.0"]
