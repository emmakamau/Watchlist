from flask import Blueprint

main = Blueprint('main',__name__)

#from main import views,error

from . import views, error