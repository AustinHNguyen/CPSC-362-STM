from flask import Blueprint, render_template
route = Blueprint('views', __name__)

@route.route('/')
def home_page():
    return render_template("homepage.html")