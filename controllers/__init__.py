from flask import Blueprint

#############################################
## USE THIS FILE TO DEFINE ANY Routes
## Create Sub Blueprints as needed
#############################################

home = Blueprint("home", __name__)

@home.get("/")
def home_home():
    return {"home": "this is the home route"}