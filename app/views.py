"""
   1. We import the render_template() function from Flask. This function takes in the name of a template file as the first argument. It then automatically searches for the template file in our app/templates/ sub directory and loads it.
"""

from flask import render_template
from app import app

# Views
@app.route('/')  #route decorator
def index():  #view function
   
   message = 'Hello World'
   return render_template('index.html')

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    return render_template('movie.html',id = movie_id)
