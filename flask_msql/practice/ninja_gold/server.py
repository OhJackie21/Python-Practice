from flask import Flask, render_template, redirect, session, request
import random
import datetime

app = Flask(__name__)
app.secret_key = "holy fudge"

@app.route('/')
def index():
    if "gold_qty" not in session:
        session['gold_qty'] = 0
    if "activity" not in session:
        session['activity'] = []

    return render_template("index.html", gold_qty = session['gold_qty'], activity=session['activity'])

@app.route('/process_money', methods=['POST'])
def process():
    time = datetime.datetime.now()
    if request.form.get('property') == "farm":
        gold = random.randint(10,20)
        session['gold_qty'] += gold
        activity = f"You've earned {gold} golds by Farming @ {time}"
        session['activity'].append(activity)


    if request.form.get('property') == "cave":
        gold = random.randint(5,10)
        session['gold_qty'] += gold

    if request.form.get('property') == "house":
        gold = random.randint(2,5)
        session['gold_qty'] += gold

    if request.form.get('property') == "casino":
        gold = random.randint(-50,50)
        session['gold_qty'] += gold
    
    return redirect('/')



@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)