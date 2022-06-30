FROM python:3.9-slim
LABEL MAINTAINER="Mohammad Javad Nikbakht | javadnikbakht@mail.com"

ENV PYTHONBUFFERED 1

# Set working directory
RUN mkdir /escrow
WORKDIR /escrow
COPY . .

# Installing requirements
ADD requirements.txt /escrow
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Migrating Database
RUN python manage.py makemigrations products
RUN python manage.py migrate

#Collect static files
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "escrow", "--bind", ":8000", "escrow.wsgi:application"]


