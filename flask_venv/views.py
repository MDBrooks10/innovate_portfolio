from flask import render_template, redirect, Blueprint

my_view = Blueprint('my_view', __name__)

@my_view.route("/")
def home():
    return render_template("home.html")

@my_view.route("theman")
def theman():
    return render_template("theman.html")

@my_view.route("thedog")
def thedog():
    return render_template("thedog.html")

@my_view.route("thevan")
def thevan():
    return render_template("thevan.html")

