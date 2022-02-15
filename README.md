# loan_api

## Installation
After cloning the repo using either ssh or http,depending on your pip configurations install project dependencies with pip/pip3.

```bash
$ git clone git@github.com:Abbracx/loan_api.git
```

OPTIONAL
```bash
$ pip install -r requirements.txt
```


NOTE: It is assumed you already have a virtual environment running. 
Click the link [here](https://towardsdatascience.com/why-you-need-a-python-virtual-environment-and-how-to-set-it-up-35019841697d) on how to setup and work with a virtual environment
## Running loan container mysql docker container with docker-compose
These project was dockerize and uses the mysql docker container as the database service.
Link to the loan image registry will be updated soon...

```bash
$ docker-compose up -d --build
```
After container spins up, head tp ```localhost:8000``` to navigate your routes.

1. ```localhost:8000/login```
2. ```localhost:8000/logout```
3. ```localhost:8000/users```
4. ```localhost:8000/user```
Other endpoints will be updated as project progresses.


## Test

```bash
# unit tests
python3 manage.py test
```

## Social links

- PORTFOLIO - [Ralph Abbrac'x](https://abbracx.github.io/Portfolio/)
- LINKEDIN - [Ralph Abbrac'x](https://www.linkedin.com/in/raphael-tanko-172195137/)
- TWITTER - [@abbrac_x](https://twitter.com/abbrac_x)
