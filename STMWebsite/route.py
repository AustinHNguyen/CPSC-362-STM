from flask import Blueprint
route = Blueprint('views', __name__)

@route.route('/')
def home_page():
    return "<h1>Student Task Manager</h1>"