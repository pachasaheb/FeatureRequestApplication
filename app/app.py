# Flask is a Python class datatype.Flask  is the prototype used to create instances of web application or web applications.
from flask import Flask
# imports Config class from config.py module
from config import Config
# once we import Flask, we need to create an instance of the Flask class for our web app.
# passing __name__ is going to configure Flask.
# __name__ is a special variable that gets as value the string "__main__" when you’re executing the script.
APP = Flask(__name__)
# APP a flask variable gets database configurations from config.py file
APP.config.from_object(Config)
# importing routes.py, featureRequestManager.py, featureRequestService.py, models.py
#Imports all the reamining modules required for project.
from models import FeatureRequestApp
import featureRequestManager, featureRequestService, routes
