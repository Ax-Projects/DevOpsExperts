FROM python:3.9-alpine

WORKDIR /app
COPY db_connector.py rest_api.py requirements.txt clean_environment.py clean_db.py /app/

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3", "rest_api.py" ]