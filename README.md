# Simple API gateway using python-zeroconf

Sample implementation of an API gateway with automatic service discovery using the `python-zeroconf` library. Both gateway and services
are executed in different Docker containers.

### Usage

In order to execute this code you should have the Docker daemon running on your environment and also the `docker-compose` utility
installed. For running the API gateway and two sample services just execute:
```
docker-compose up -d
```

Sample information on the automatically discovered services can be accessed at `http://0.0.0.0:4999/services`. 

### Purpose

This is only a sample implementation but it can be used as blueprint for much more complicated programs which use a microservice architecture. Beware that
that the services must be developed in Python.
