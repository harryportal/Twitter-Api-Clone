# Twitter-Api-Clone
This is an Implementation of Twitter's Api with Django Rest Framework:rocket:
***
To run on a development server with a default sqlite database, clone the repository and run the following command in your terminal
```sh
$:git clone https://github.com/harryportal/Twitter-Api-Clone
$:cd tweeter 
tweeter$:pip install requirements.txt
tweeter$:python manage.py migrate
tweeter$:python manage.py runserver
```
Use the pytest command to executes the test 
```sh
tweeter$:pytest
```
To test the endpoints on postman, follow these easy steps:
- Import the postm an collection from /tweeter
- Test the create user endpoint to create a new user
- Test the /get-token endpoint to get a JWT Token that will be used to authenticate other endpoints

