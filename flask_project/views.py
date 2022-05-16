from flask import render_template, redirect, Blueprint, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route("/")
def home():
    return render_template("home.html")

@my_view.route("/theman")
def theman():
    return render_template("theman.html")

@my_view.route("/thedog")
def thedog():
    return render_template("thedog.html")

@my_view.route("/thevan")
def thevan():
    return render_template("thevan.html")

# @my_view.route("/thevan", methods=["GET","POST"])
# def about():
#     if request.method == "POST":
#         try:
#             id == "song_add"
#             new_song = request.form["add_song"]
#             add_to_list(new_song)
#         except:
#             id == "song_delete"
#             remove_song = request.form["delete_song"]
#             delete_from_list(remove_song)
#     return render_template("thevan.html", songs=empty)

@my_view.route("/home")
def home_redirect():
    return redirect(url_for("my_view.home"))

@my_view.route("/homepage")
def homep_redirect():
    return redirect(url_for("my_view.home"))