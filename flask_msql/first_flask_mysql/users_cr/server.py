from flask import Flask, render_template,redirect,request
from users import Users

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/info')

@app.route('/info')
def user_info():
    users = Users.get_all()
    print(users)
    return render_template("userinfo.html", users=users)

@app.route('/users/new')
def newuser():
    return render_template("index.html")

@app.route('/users/create', methods=['POST'])
def adduser():
    print(request.form)
    Users.save(request.form)
    return redirect('/info')

if __name__ == "__main__":
    app.run(debug=True)