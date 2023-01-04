from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = "secret lover"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    session['fname'] = request.form['fname']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return render_template('results.html')

@app.route('/back', methods=['POST'])
def back():
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)   