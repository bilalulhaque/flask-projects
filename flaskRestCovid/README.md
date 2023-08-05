# Flask-restful-API for Covid Data
Created a Restful API in Flask that provides a few CRUD endpoints for the sample covid data. In this project I've mainly focused on authentication/authorization, security, documentation using Swagger, and testing. I've stored confidential credentials in a .env file and login credentials are stored in environment variables of the system.

Following are the steps to run the project:

1. #### Set credentials for login in environment variables
```
user_email = your email
user_password = your password
```
2. #### Configure the .env.test file
```
set envFile = location of file
```
3. #### Install Libraries 
```
pip install -r requirements.txt
```
4. #### Run the server
```
python app.py
```

Following are the steps to run the tests:
1. #### To run the sign in test
```
python -m unittest tests/test_signIn.py
````
2. #### To run the add data test
```
python -m unittest tests/test_add_daily_data.py
````
3. #### To run all the tests at once use the command
```
python -m unittest --buffer
```
