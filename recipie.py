from flask import Flask  # import flask

app = Flask(__name__)


@app.route("/")
def hello():
    return f"HomePage"


@app.route("/<name>")
def hello_name(name):
    return "Hello, " + name


if __name__ == "__main__":
    # app.run()  # run the flask app
    app.run(host='0.0.0.0', debug=True)
