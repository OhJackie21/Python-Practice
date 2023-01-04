from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', num1 = 3, num2 = 3,color1 = "red", color2 = "blue")

@app.route('/board/<int:num1>')
def row(num1):
    return render_template('index.html', num1 = num1, num2 = num1, color1 = "red", color2 = "blue" )

@app.route('/board/<int:num1>/<int:num2>')
def mult_row(num1,num2):
    return render_template('index.html', num1 = num1, num2 = num2, color1 = "red", color2 = "blue")

@app.route('/board/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def mult_color(num1,num2,color1,color2):
    return render_template('index.html', num1 = num1, num2 = num2, color1 = color1, color2 = color2)


if __name__=="__main__":
    app.run(debug=True)