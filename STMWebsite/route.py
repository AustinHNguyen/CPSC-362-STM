from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Note
from .models import User
from . import db
from flask_sqlalchemy import SQLAlchemy

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
    noteId = note['noteId']
    note = Note.query.get(noteID)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})

@route.route('/save_text', methods=['POST'])
@login_required
def save_text():
    data = request.get_json()
    task = data['text']
    current_user.text = task
    db.session.commit()
    return jsonify({'message': 'Text saved successfully'})