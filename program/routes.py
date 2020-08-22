from program.user import User
from program import app
from program.forms import LoginForm
from flask import render_template, flash, redirect


@app.route('/')
@app.route('/index')
def index():
    user = User(username="Bob", password_hash="password", email="bob@email.com")
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route("/show-user")
def show_user():
    recipe_dict1 = {
        "name": "Fried Eggs",
        "ingredients": ["eggs", "oil", "salt", "pepper"],
        "time": 15  # in minuets

    }
    recipe_dict2 = {
        "name": "Cereal",
        "ingredients": ["cereal", "milk", "bowl", "spoon"],
        "time": 2  # in minuets

    }
    u = User()
    u.first_name = "Bob"
    u.user_name = "bob123"
    u.password = "password"
    u.id = 1
    u.recipes.append(recipe_dict1)
    u.recipes.append(recipe_dict2)

    return render_template('index.html', title=f"{u.first_name}'s Recipes", user=u, posts=u.recipes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect("/")
    return render_template('login.html', title='Sign In', form=form)
