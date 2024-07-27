FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./wait-for-it.sh /code/wait-for-it.sh

COPY ./.env /code/.env

RUN chmod +x /code/wait-for-it.sh
