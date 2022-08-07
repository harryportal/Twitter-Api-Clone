# Twitter-Api-Clone
This is an simple Twitter Api Clone built with Django Rest Framework:rocket:
***
To run on a development server: 
```sh
> git clone https://github.com/harryportal/Twitter-Api-Clone
> cd tweeter
> pip install requirements.txt
```
This creates and populate the sqlite database with user and tweets data:
```sh
> python manage.py migrate
> python manage.py tweet_user_data 
```
Use the pytest command to executes the test 
```sh
> pytest
```
Start the server with `python manage.py runserver`
***
Follow these easy steps to test all the endpoints:
- Import the postman collection from /tweeter(if you have postman installed) or simply use the Swagger Ui(the API's homepage)
- Test the create user endpoint to create a new user
- Test the /get-token endpoint to get a JWT Token that will be used to authenticate other endpoints


UPDATES:
- [ ] Liking and Unliking a comment
- [ ] comment on other comments(nested comments)
- [ ] support chatting using Django channels for websockets
- [ ] Use redis for caching
- [ ] Displaying retweeted tweets in feed

