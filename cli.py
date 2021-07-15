#############################################
## USE THIS FILE TO DEFINE ANY CLI COMMANDS
## Define each command in the create_cli function
#############################################

def create_cli(app):
    ## python cli.py    
    ## FLASK_APP=sever.py python -m flask default_command
    @app.cli.command("default_command")
    def cli_default():
        print("Hello World")