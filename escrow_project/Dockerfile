# pull official base image
FROM python:3.9.5-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variablessh /usr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# postgres
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --update --no-cache postgresql-client jpeg-dev



# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh

RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x  /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
