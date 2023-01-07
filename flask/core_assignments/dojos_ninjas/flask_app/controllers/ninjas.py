from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/addninja')
def addform():
    dojos = Dojo.get_all()
    return render_template('addninja.html', dojos = dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    Ninja.addninja(request.form)
    return redirect('/home')

@app.route('/update_ninja', methods=['POST'])
def update_ninja():
    Ninja.update(request.form)
    return redirect('/home')

# @app.route('/edit_ninja/<int:id>')
# def edit_ninja(id):
#     data = { "id":id}
#     return render_template('update.html', ninja = Ninja.ninja_info(data), dojos = dojo.Dojo.ninjas_in_dojo(data) )

@app.route('/edit_ninja/<int:id>')
def ninja_names(id):
    data = { "id": id } 
    ninja = Ninja.ninja_info(data)
    dojos = Dojo.get_all()
    return render_template('update.html', ninja = ninja, dojos=dojos)

@app.route('/delete/<int:id>')
def delete_ninja(id):
    data = { "id": id }
    Ninja.delete_ninja(data)
    return redirect('/home')