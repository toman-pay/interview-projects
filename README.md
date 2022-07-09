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
14. lint hooks(flake8 and auto-sort)

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
http://localhost:8000/api/

## Swagger file
Please refer to swagger file in the root of the project for more information about API.

## Postman collection
Feel free to use postman collection as API example and docs:

## Licence
Let's look forward licence later ;)
Please feel free to send me email Mortaz.Mehdi@gmail.com