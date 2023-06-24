FROM python:3.9-alpine

WORKDIR /app
COPY db_concector.py rest_api.py requirements.txt clean_environment.py /app/

ENV DBHOST=${DBHOST} DBUSER=${DBUSER} DBPASSWORD=${DBPASSWORD} DB=${DB} SCHEMA=${SCHEMA} PORT=${PORT}
CMD ["pip", "install -r requirements.txt"]

EXPOSE 5000

ENTRYPOINT [ "python3", "rest_api.py" ]