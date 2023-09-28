from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template("login.html") 

@auth.route('/logout')
def logout():
    return "<h>Logout</h>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password')
        confirmPass = request.form.get('confirmPass')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category = 'error')
            pass
        elif len(firstName) < 2:
            pass
        elif password != confirmPass:
            flash('passwords do not match.', category = 'error')
            pass
        elif len(password < 7):
            pass
        else:
            pass

    return render_template("signup.html")