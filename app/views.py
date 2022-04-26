"""
   1. We import the render_template() function from Flask. This function takes in the name of a template file as the first argument. It then automatically searches for the template file in our app/templates/ sub directory and loads it.
"""

from flask import render_template
from app import app
from .request import *

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

@app.route('/movie/<int:id>')
def movie(id):

   movie = get_movie(id)
   title = f'{movie.title}'
   return render_template('movie.html',title=title, movie=movie)
