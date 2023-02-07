from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return redirect('/index')

@app.route('/index')
def main():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.user_validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    id = User.register(data)
    session['user_id'] = id
    return redirect('/home')

@app.route('/home')
def dash():
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 'id': session['user_id']}
    user = User.user_info(data)
    shows = Show.all_shows()
    return render_template('home.html', user=user, shows=shows)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = { "email": request.form['email'] }
    user_in_db = User.email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/home')