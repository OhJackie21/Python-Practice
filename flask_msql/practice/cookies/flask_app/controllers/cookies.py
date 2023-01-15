from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.cookie import Cookie

@app.route('/')
def index():
    return redirect('/orders')

@app.route('/orders')
def orders():
    session.pop('customer_name', None)
    session.pop('cookie_type', None)
    session.pop('order_qty', None)
    cookies = Cookie.all()
    return render_template('index.html', cookies = cookies)

@app.route('/edit/<int:id>')
def edit(id):
    data = { "id": id }
    cookies = Cookie.order_info(data)
    return render_template('edit.html', cookies = cookies)

@app.route('/update', methods=['POST'])
def update():
    if not Cookie.validate_add(request.form):
        return redirect(f"/edit/{request.form['id']}")
    Cookie.update(request.form)
    return redirect('/')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/add', methods = ['POST'])
def add():
    if not Cookie.validate_add(request.form):
        session['customer_name'] = request.form['customer_name']
        session['cookie_type'] = request.form['cookie_type']
        session['order_qty'] = request.form['order_qty']
        return redirect('/order')

   
    Cookie.add(request.form)
    return redirect('/')