from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "keywillbechanged"

#Creating a form class
class Namerform(FlaskForm):
    name = StringField("Whats your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


#Create a route decorator
@app.route('/')

#def index():
    #return "<h1> HelloWorlds</h>"

def index():
    first_name = "Jphn"
    return render_template("index.html", first_name=first_name)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)



#Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = Namerform()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("name.html", name=name, form=form)







#Custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500