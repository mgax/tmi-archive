FROM python:3.8
WORKDIR /app

COPY Pipfile Pipfile.lock .
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

CMD ./manage.py runserver 0:8000
