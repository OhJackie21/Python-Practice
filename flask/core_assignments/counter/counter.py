from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = "chocolate fudge"  

@app.route('/')         
def index():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 0
    return render_template("index.html")

@app.route('/add2')         
def index2():
    if "count" in session:
        session["count"] += 1
    return redirect("/")
    
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)   