# syntax = docker/dockerfile:experimental
FROM python:3.8
ENV PYTHONBUFFERED 1

# install requirements, use cache
COPY requirements.txt .
# RUN --mount=type=cache,target=~/.cache/pip pip install -r requirements.txt
RUN pip install -r requirements.txt

# Now copy all codes and local_package
COPY . .
