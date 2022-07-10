#Screw account restful Application
An escrow is a contractual arrangement in which a third party (the stakeholder or escrow agent) receives and disburses
money or property for the primary transacting parties, with the disbursement dependent on conditions agreed to by the
transacting parties.

## Stack Description
This app wrote with the Django framework which is integrated/used with:
1. DRF
2. JWT
3. Celery
4. Redis
5. Rabbitmq
6. Postgresql
7. Docker & docker compose
8. Swagger
9. Sentry
10. Postman
11. Collection
12. Test
13. pre-commit
14. Pre-commit lint hooks
15. CORS handling
16. Nginx for serving static/media files in production and Whitenoise for development.
17. Grafana, prometheus for visualize and metrics
18. Custom middleware to convert exception to API status (I love it!)
19. Factory boy

## Dependency
To run in production level, needs to have docker and docker-compose
```text
docker
docker-compose
```
### Dependency installation

Quick and easy installation script provided by Docker:

```shell script
curl -sSL https://get.docker.com/ | sh
```
To install docker-compose on Debian base OS:
```shell script
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

```
If you're not willing to run a random shell script, please see the [installation](https://docs.docker.com/engine/installation/linux/) instructions for your distribution.

If you are a complete Docker newbie, you should follow the [series of tutorials](https://docs.docker.com/engine/getstarted/) now.

## Test
go to project's root directory and execute following commands:
```shell script
cd apps
./manage.py test
```

## Run
clone the git repository and got to project's root directory in the terminal and run following command:
```shell script
sudo docker-compose up --build -d
```
Brows following url to check the URL docs:
[http://localhost:80/swagger/](http://localhost:80/swagger/)

## Swagger file
Please refer to swagger file in the root of the project for more information about API.

## Postman collection
Feel free to use postman collection as API example and docs:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/9d79795edc4869d7b89b?action=collection%2Fimport#?env%5BDev%5D=W3sia2V5Ijoic2VydmVyX3VybCIsInZhbHVlIjoiaHR0cDovLzAuMC4wLjA6ODAwMCIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoiYWNjZXNzX3Rva2VuIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6InJlZnJlc2hfdG9rZW4iLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoiYm90X3VybCIsInZhbHVlIjoiaHR0cDovL2xvY2FsaG9zdDo4MDAwIiwiZW5hYmxlZCI6dHJ1ZX1d)

## Licence
Let's look forward licence later ;)
Please feel free to send me email Mortaz.Mehdi@gmail.com
