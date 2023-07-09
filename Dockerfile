FROM python:3.9-alpine

WORKDIR /app
COPY rest_api.py requirements.txt clean_environment.py clean_db.py /app/
COPY db_connector_docker.py /app/db_connector.py 

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3", "rest_api.py" ]