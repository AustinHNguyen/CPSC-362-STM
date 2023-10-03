from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def web_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CPSC362'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    from .route import route
    from .auth import auth

    app.register_blueprint(route, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Task

    create_database(app)
    return app

def create_database(app):
    if not path.exists('STMWebsite/' + DB_NAME):
        db.create_all(app=app)
    return 