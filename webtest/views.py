from flask import Blueprint, render_template, request,redirect,url_for
from .models import User, Write
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET','POST'])
def utama():
    user = User.query.all()
    if request.method == 'POST':
        nama = request.form.get('nama')
        kelamin = request.form.get('kelamin')
        email = request.form.get('email')

        new_note = User(name = nama, kelamin = kelamin, email= email)
        db.session.add(new_note)
        db.session.commit()

        return redirect(url_for('views.utama', user = user))
    return render_template("utama.html" ,user = user)


from datetime import datetime

@views.route('/konten/<index>', methods = ['GET','POST'])
def konten_detail(index):
        konten = Write.query.filter_by(user_id = index).all()
        date = []
        tulis = []
        id = []
        for i in konten:
            date.append((i.date).strftime("%d/%m/%Y %H:%M:%S"))
            tulis.append(i.tulis)
            id.append(i.id)
        user = User.query.filter_by(id = index).first()
        if request.method == 'POST':
            konten = request.form.get('tulis')
            now = datetime.now()
            new_note = Write(tulis=konten, date = now, user_id = index)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('views.konten_detail', index = index))
        return render_template("konten.html",us = user, date = date, tulis = tulis, len = len(date), id = id)


@views.route('/edit_user/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        my_data = User.query.get(id)

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.kelamin = request.form['kelamin']

        db.session.commit()

        return redirect(url_for('views.utama'))

@views.route('/delete_user/<x>', methods = ['GET','POST'])
def user_delete(x):
    unit = User.query.filter_by(id = x).all()
    for un in unit:
        db.session.delete(un)
        db.session.commit()
    return redirect(url_for('views.utama'))

@views.route('/delete_konten/<user>/<x>', methods = ['GET','POST'])
def konten_delete(user,x):
    konten = Write.query.get(x)
    db.session.delete(konten)
    db.session.commit()
    return redirect(url_for('views.konten_detail', index = user))
