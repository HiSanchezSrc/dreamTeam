from app import app

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')








@app.route("/create-recipe")
def recipe_form():
    pass


# if __name__ == "__main__":
#     # app.run()  # run the flask app
#     app.run(host='0.0.0.0', debug=True)
