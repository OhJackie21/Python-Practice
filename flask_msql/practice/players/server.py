from flask import Flask, render_template, redirect, session, request
from players import Players

app = Flask(__name__)
app.secret_key = "unholy"

@app.route('/')
def index():
    return redirect('/info')

@app.route('/info')
def player_info():
    players = Players.get_all()
    print(players)
    return render_template('index.html', players=players)

@app.route('/addplayer')
def click():
    return render_template('add.html')

@app.route('/add_user', methods=['POST'])
def add_player():
    print(request.form)
    Players.save(request.form)
    return redirect('info')

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


if __name__=="__main__":
    app.run(debug=True)
