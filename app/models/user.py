from datetime import datetime

from app import db


def parse_recipes(recipe_list):
    recipe_string = ""
    for recipe_dict in recipe_list:
        name = recipe_dict["name"]
        ingredients = recipe_dict["ingredients"]
        time = recipe_dict["time"]
        recipe_string += f"{name},\r\n Ingredients: {ingredients}, \r\nReady in {time} minuets\r\r"
    return recipe_string


# class User:
#
#     def __init__(self):
#         self.id = None
#         self.first_name = None
#         self.user_name = None
#         self.password = None
#         self.recipe = {}
#         self.recipes = []
#
#     def show_data(self):
#         user_data = f"{self.first_name} {self.lastName}, Recipes: {parse_recipes(self.recipes)}  "
#         return user_data


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    recipes = db.relationship('Recipe', backref='name', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    name = db.Column(db.String(32))
    ingredients = db.Column(db.String(140))
    time = db.Column(db.Integer)
    body = db.Column(db.String(500))

    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Recipe {}>'.format(self.body)
