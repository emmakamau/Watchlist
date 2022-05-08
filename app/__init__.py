from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE
from flask_mail import Mail

login_manager = LoginManager()
bootstrap = Bootstrap()
simple = SimpleMDE()
db = SQLAlchemy()
mail = Mail()

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    # configure UploadSet
    configure_uploads(app,photos)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Blueprint for user authentication
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # setting config
    from .request import configure_request
    configure_request(app)


    return app