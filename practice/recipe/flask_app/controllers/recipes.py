from flask import render_template, redirect, session, request,flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


@app.route('/create')
def create():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create.html')

@app.route('/addrecipe', methods=['POST'])
def addrecipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/create')
    
    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instruction': request.form['instruction'],
        'date_made': request.form['date_made'],
        'under_30': request.form['under_30']
    }
    Recipe.add_recipe(data)
    return redirect('/dash')

@app.route('/edit_recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = { 'id': id }
    recipe = Recipe.getidby(data)
    print(recipe)
    return render_template("editrecipe.html", recipe = recipe)


@app.route('/update', methods = ['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/edit_recipe/{request.form['id']}")
    Recipe.update_recipe(request.form)
    return redirect('/dash')

@app.route('/view/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe_data = { 'id': id }
    user_data = { 'id': session['user_id'] }
    recipe = Recipe.getidby(recipe_data)
    user = User.user_info(user_data)
    # print(recipe.user_id, "A"*20)
    recipe_owner = { 'id': recipe.user_id }
    rec_own = User.user_info(recipe_owner)
    return render_template('view.html', recipe=recipe, user=user, rec_own=rec_own)


@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = { 'id': id }
    Recipe.remove_recipe(data)
    return redirect('/dash')
  