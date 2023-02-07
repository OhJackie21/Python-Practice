from flask import render_template, redirect, session, request,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.show import Show

@app.route('/addnewshow', methods=['POST'])
def addrecipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Show.validate_show(request.form):
        return redirect('/addshow')
    data = {
        'user_id': session['user_id'],
        'title': request.form['title'],
        'network': request.form['network'],
        'release_date': request.form['release_date'],
        'description': request.form['description'],
    }
    Show.add_show(data)
    return redirect('/home')

@app.route('/addshow')
def create():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('addshow.html')

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data = { 'id': id }
    show = Show.getidby(data)
    return render_template("editshow.html", show=show)
    
@app.route('/view/<int:id>')
def view_show(id):
    if 'user_id' not in session:
        return redirect('/')
    show_data = { 'id': id }
    user_data = { 'id': session['user_id'] }
    show = Show.getidby(show_data)
    user = User.user_info(user_data)
    show_owner = { 'id': show.user_id }
    show_own = User.user_info(show_owner)
    return render_template('view.html', show=show, user=user, show_own=show_own)


@app.route('/update', methods = ['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/')
    if not Show.validate_show(request.form):
        return redirect(f"/edit/{request.form['id']}")
    Show.update_show(request.form)
    return redirect('/home')

@app.route('/delete/<int:id>')
def delete_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data = { 'id': id }
    Show.remove_show(data)
    return redirect('/home')