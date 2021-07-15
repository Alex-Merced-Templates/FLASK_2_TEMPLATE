## Flask Template

### Setup

- create a virtual environment `python -m venv venv` (if you use another name, adjust .gitignore)

- enable virtual env `source ./venv/bin/activate`

- install dependencies `pip install -r requirements.txt`

### COMMANDS

- Running Server: `python server.py` or `FLASK_APP=server.py python -m flask run`

- Running CLI Commands: `FLASK_APP=server.py python -m flask <command name>`

### CONFIG

All of the properties defined in the dictionary config/__init__.py will be part of the app.config object. Feel free to add more. If you want the properties to be read from a .env file make sure to pass the USE_DOTENV env variable. `USE_DOTENV=True python server.py`

### Routes

Routes are written in the controllers folder

### Models 

The models folder available if you decide to use an ORM

### CLI Commands

Define CLI commands in the function in the cli.py file

### Procfile

The Procfile for Heroku deployment is included