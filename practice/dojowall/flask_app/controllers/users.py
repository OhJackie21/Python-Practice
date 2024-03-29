from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def main():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validated_add(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    
    id = User.register(data)
    session['user_id'] = id
    return redirect('/wall')

@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 'id': session['user_id'] }
    users = User.getid(data)
    return render_template("wall.html", users=users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    data = { 'email': request.form['email'] }
    userdb = User.getemail(data)
    if not userdb:
        flash('Invalid Email','invalid')
        return redirect('/')
    if not bcrypt.check_password_hash(userdb.password, request.form['password']):
        flash('Invalid Password', 'invalid')
        return redirect('/')
    
    #if password matches, set user_id into session
    session['user_id'] = userdb.id
    return redirect('/wall')

