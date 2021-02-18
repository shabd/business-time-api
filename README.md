# business-time-api
Application Built By : Shabd Maharaj 
An API end point that will calculate the total number of business seconds between two given times

The Application is Run inside of a docker container:
To start application : docker-compose run app sh -c "python manage.py runserver"

The End-point url is :
http://127.0.0.1:8000/business/<start_time>/<end_time>/

The End Point Supports ISO-8601 time format , and example of a query:

http://127.0.0.1:8000/business/start_time=2021-02-17T08:00:00+0000/end_time=2021-02-17T17:00:00+0000/
