from flask import Flask, render_template
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def test():
    query = """INSERT into users (first_name, last_name, email, password, user_level, description, created_at, updated_at)
            values ("jackie", "oh", "jac@j.com", "joj", 1, "blah", now(), now() )"""
    connectToMySQL('user_dashboard_schema').query_db(query)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)