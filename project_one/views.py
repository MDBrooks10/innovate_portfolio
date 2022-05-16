from flask import render_template, redirect, Blueprint, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page1")
def page1():
    return render_template("page1.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html")
                                                    #Links to 5+ different web pages
@my_view.route("/page3")
def page3():
    return render_template("page3.html")

@my_view.route("/page4")
def page4():
    return render_template("page4.html")

@my_view.route("/admin")
def pageadmin():                                    #Admin redirect to admin page
    return render_template("admin.html")

@my_view.route("/javascript")                        #Redirects for javascript, js and home
@my_view.route("/js")
@my_view.route("/home")
def index_redirect():
    return redirect(url_for("my_view.index"))