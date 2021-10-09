# YASON - JSON-TO-YAML & YAML-TO-JSON CONVERTER
ABOUT: This is an API that can take in YAML and converts it to JSON and can take JSON and convert it to YAML. **There is no frontend yet :)**

## STACK
* language: Python3
* Framework: Django
* Infrastructure: Docker

## Code
Django framework is used to build this API. Tests are also done with the Framework's test suite.

## TESTING
* In order to run the tests for the application locally run ```python3 manage.py test```. This is also included in the docker build step to ensure only code that passed tests is built.

## Running locally
To run the code locally (out of docker)
* Test with ```python3 manage.py test```
* Start API with ```python3 manage.py runserver 0.0.0.0:8080```

## ACCESS API ENDPOINTS (LOCALLY)
To access the API, you can use PostMan or any other HTTP Client of your choice.

* To convert JSON to YAML - make a ```POST``` request to http://localhost:8080/api/yason/json-to-yaml with the JSON Text to be converted as Body of the request.

* To convert YAML to JSON - make a ```POST``` request to http://localhost:8080/api/yason/yaml-to-json  with the YAML Text to be converted as Body of the request.

* Health Check - To continously check the application for uptime, make a ```GET``` request to http://127.0.0.1:8080/api/yason/health. This endpoint should return a 200 Status OK to show that the API is healthy.

## TODO
* Create a frontend to make the API more user friendly.