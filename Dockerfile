FROM python:3.6
MAINTAINER @repodevs <iam@fromindonesia.id>

ENV APP_PATH /usr/src/app

RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD ["gunicorn", "core.wsgi:app", "--bind", "0.0.0.0:8338"]
