from flask import render_template, redirect, session, request
from flask_app.models.players import Players
from flask_app import app



@app.route('/')
def index():
    return redirect('/info')

@app.route('/info')
def player_info():
    players = Players.get_all()
    print(players)
    # if "first_name" in i:
    #     print("practice")
    return render_template('index.html', players=players)

@app.route('/addplayer')
def click():
    return render_template('add.html')

@app.route('/add_user', methods=['POST'])
def add_player():
    if not Players.validate_add(request.form):
        return redirect('/addplayer')
    print(request.form)
    Players.save(request.form)
    return redirect('/info')

@app.route('/edit/<int:id>')
def edit(id):
    data = { "id": id}
    return render_template('edit.html', players=Players.player_info(data))

@app.route('/update', methods=['POST'])
def update():
    Players.update(request.form)
    return redirect('/info')

@app.route('/show/<int:id>')
def show(id):
    data = { "id": id}
    return render_template('info.html', players = Players.player_info(data))

@app.route('/delete/<int:id>')
def delete(id):
    data = { "id": id }
    Players.remove(data)
    return redirect('/info')
