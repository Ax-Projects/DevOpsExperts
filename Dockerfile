FROM python:3.9-alpine

COPY db_concector.py rest_api.py requirements.txt clean_environment.py /code/

CMD ["pip install -r requirements.txt"]

ENTRYPOINT [ "python3 " ]