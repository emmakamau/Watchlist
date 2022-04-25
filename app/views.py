"""
   1. We import the render_template() function from Flask. This function takes in the name of a template file as the first argument. It then automatically searches for the template file in our app/templates/ sub directory and loads it.
"""

from flask import render_template
from app import app
from .request import get_movies

# Views
@app.route('/')  #route decorator
def index(): #view function

   '''
   View root page function that returns the index page and its data
   '''

   # Getting popular movie
   popular_movies = get_movies('popular')
   upcoming_movie = get_movies('upcoming')
   now_showing_movie = get_movies('now_playing')
   title = 'Home - Welcome to The best Movie Review Website Online'
   return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

   title = 'Movie list'
   return render_template('movie.html',title=title, id = movie_id)
