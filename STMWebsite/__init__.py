from flask import Flask

def web_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CPSC362'
    from .route import route
    from .auth import auth

    app.register_blueprint(route, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
