import flask
from cli import create_cli
from controllers import home
from config import config

#############################################
## This function sets up the app object
## 
#############################################

def create_app(name):
    ## Create APP Object
    app = flask.Flask(name)

    ## Update Config Values
    app.config.update(**config)

    ## Register Routes through the Home Blueprint
    app.register_blueprint(home)

    ## Register CLI COMMANDS
    create_cli(app)

    return app