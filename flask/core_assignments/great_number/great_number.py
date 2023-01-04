from flask import Flask, render_template, request, redirect,session
import random

app = Flask(__name__)

app.secret_key = "secret wow"

@app.route('/')
def main():
    if "randnum" not in session:
        session['randnum'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def num_guess():
    session['num_guess'] = int(request.form['num_guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    
if __name__=="__main__":   
    app.run(debug=True)  