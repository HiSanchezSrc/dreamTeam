from flask import Flask  # import flask
from user import *

app = Flask(__name__)


@app.route("/")
def hello():
    return f"HomePage"


@app.route("/<name>")
def hello_name(name):
    return "Hello, " + name


@app.route("/showUser")
def show_user():
    recipieDict1 = {
        "name": "Fried Eggs",
        "ingredients": ["eggs", "oil", "salt", "pepper"],
        "time": 15  # in minuets

    }
    recipieDict2 = {
        "name": "Cereal",
        "ingredients": ["cereal", "milk", "bowl", "spoon"],
        "time": 2  # in minuets

    }
    u = User()
    u.firstName = "Bob"
    u.lastName = "Smith"
    u.id = 1
    u.recipes.append(recipieDict1)
    u.recipes.append(recipieDict2)

    return u.show_data()


if __name__ == "__main__":
    # app.run()  # run the flask app
    app.run(host='0.0.0.0', debug=True)
