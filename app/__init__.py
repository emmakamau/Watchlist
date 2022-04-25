from flask import Flask #import the Flask class from flask module
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config = True) #create an app instance.

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views #imports everything in the views.py file