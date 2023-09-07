from flask import Flask

def web_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CPSC362'
    return app