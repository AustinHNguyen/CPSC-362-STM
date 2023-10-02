from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
    return app
