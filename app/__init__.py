from flask import Flask
from app.home.routes import home_bp
from app.webhook.routes import webhook
from .extensions import setUpDatabase 

# Creating our flask app
def create_app():

    app = Flask(__name__)
    
    app = setUpDatabase(app=app)
   
    # registering all the blueprints
    app.register_blueprint(webhook)
    app.register_blueprint(home_bp)

    
    return app
