# Getting Started


### Feature Of URL Shortner
* it will ask for a valid long url.
* url shortner will generate a short url.
* Once that generated link will be clicked, it will redirect to the original long url.
* Users can also set the Expiry date.
* The shorten link will only be valid till the expiry date.
* Cron Job scheduled for cleaning of all expired urls.


### Technology used:-
* Programming Language - python
* Web Framework (Backend) - Django Rest Framework
* Web Framework (Frontend) - React
* Database - PostgreSql
* Server - Gunicorn instead of Wsgi
* Docker, Docker-compose


### How to Clone and run locally
    git clone https://github.com/demin13/urlshortner.git

##### Web Framework (Backend)
    To Build Image
    # docker build -t url:urlshortner .

    To up the container in detached mode using docker-compose
    # docker-compose up -d
    # docker-compose up -d --build  ## to rebuild the container

    To execute the container in bash mode
    # docker exec -it urlcontainer bash

    To makemigration
    python manage.py makemigrations

    To migrate
    python manage.py migrate

    To run the gunicorn server instead of wsgi(django inbuilt)
    # gunicorn -c gunicorn_config.py SHORTENURL.wsgi:application


##### Web Framework (Frontend)
    # git clone https://github.com/demin13/urlfrontend.git


#### To generate self signed SSL/TLS

    For localhost
    # openssl req -x509 -nodes -new -keyout key.pem -out cert.pem -days 365 -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"
    

    For domain
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=yourdomain.com"

