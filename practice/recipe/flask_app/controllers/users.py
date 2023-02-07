from flask import render_template, redirect, session, request,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
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
    if not User.validate_add(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    id = User.add(data)
    session['user_id'] = id
    return redirect('/dash')

@app.route('/dash')
def dash():
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 'id': session['user_id']}
    user = User.user_info(data)
    recipe = Recipe.all_recipes()
    return render_template('dash.html', user=user, recipe=recipe)

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
    
    #if passwords match, we set the user_id into session
    session['user_id'] = user_in_db.id
    return redirect('/dash')