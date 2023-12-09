# Start

pip install requirements.txt <br>
flask --app app.run run

## Create .env File

Create a `.env` file inside the project folder and add the following content:

```shell
SECRET_KEY="your secret key"
SQLALCHEMY_DATABASE_URI="sqlite:////test.db"
FLASK_ENV=development
```

Make sure to replace `"your secret key"` with your actual secret key.

##  Run the Flask Application

To start the Flask application with the environment variables from the `.env` file, use the following command:

```shell
flask --env-file .env --app app.run run --debug
```

# Tests

run all tests
```shell
pytest
```

run all tests with coverage
```shell
coverage run -m pytest
```

see cml report

```shell
coverage report -m    
```  

generate html report 

```shell
coverage html
```  

run flake8 code style check

```shell
venv/bin/flake8 app   
```  