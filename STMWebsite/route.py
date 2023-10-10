from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

route = Blueprint('route', __name__)

@route.route('/', methods=['GET', 'POST'])
@login_required
def home_page():
    if  request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Task is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Task added!', category='success')

    return render_template("homepage.html", user=current_user)

@route.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = data['noteId']