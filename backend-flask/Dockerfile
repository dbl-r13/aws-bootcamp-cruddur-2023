FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development \
    FRONTEND_URL='*' \
    BACKEND_URL='*' \
    OTEL_EXPORTER_OTLP_ENDPOINT='https://api.honeycomb.io' \
    OTEL_EXPORTER_OTLP_HEADERS='x-honeycomb-team=${HONEYCOMB_API_KEY}' \
    OTEL_SERVICE_NAME='backend-flask'\
    AWS_DEFAULT_REGION='${AWS_DEFAULT_REGION}' \
    AWS_ACCESS_KEY_ID='${AWS_ACCESS_KEY_ID}' \
    AWS_SECRET_ACCESS_KEY='${AWS_SECRET_ACCESS_KEY}'\
    ROLLBAR_ACCESS_TOKEN="69bdbf23fd4b448b813a197c8dc2e9df"


EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]