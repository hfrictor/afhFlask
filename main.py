from flask import Flask, render_template


#Create a flask instance
app = Flask(__name__)

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


#Custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500