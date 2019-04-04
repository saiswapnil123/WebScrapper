from flask import render_template, request, url_for, redirect
from scrape import app
from scrape.scrape import genereWise

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/genre")
def search():
    genre_name = request.args.get('genre')
    print(genre_name)
    return redirect(url_for("home", genre=genre_name))
@app.route("/genre_name=/<genre>")
def home(genre):
    movies = genereWise(genre)
    movies=[x for x in movies.split("\n")]
    return render_template('dispaly_books.html',f=genre,a=movies[1],b=movies[3],c=movies[5],d=movies[7],e=movies[9])