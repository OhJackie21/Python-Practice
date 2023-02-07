from flask import render_template, redirect, session, request,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.sighting import Sighting


@app.route('/addsight', methods=['POST'])
def addrecipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Sighting.validate_sighting(request.form):
        return redirect('/report')
    data = {
        'user_id': session['user_id'],
        'location': request.form['location'],
        'scenario': request.form['scenario'],
        'date_of_sighting': request.form['date_of_sighting'],
        'qty_of_sq': request.form['qty_of_sq'],
    }
    Sighting.add_sighting(data)
    return redirect('/home')

@app.route('/report')
def create():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('report.html')

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data = { 'id': id }
    sighting = Sighting.getidby(data)
    return render_template("edit.html", sighting = sighting)


@app.route('/view/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    sighting_data = { 'id': id }
    user_data = { 'id': session['user_id'] }
    sighting = Sighting.getidby(sighting_data)
    user = User.user_info(user_data)
    sighting_owner = { 'id': sighting.user_id }
    sight_own = User.user_info(sighting_owner)
    return render_template('view.html', sighting=sighting, user=user, sight_own=sight_own)

@app.route('/update', methods = ['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/')
    if not Sighting.validate_sighting(request.form):
        return redirect(f"/edit/{request.form['id']}")
    Sighting.update_sightings(request.form)
    return redirect('/home')


@app.route('/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = { 'id': id }
    Sighting.remove_sighting(data)
    return redirect('/home')