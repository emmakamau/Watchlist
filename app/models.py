from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))

    '''
    generating_password_hash - This function takes in a password and generates a password hash.
    check_password_hash - This function takes in a hash password and a password entered by a user and checks if the password matches to return a True or False response.
    '''
    pass_secure  = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    '''
    The first one is the class that we are referencing which is User. Next backref allows us to access and set our User class. We give it the value of role now because when we want to get the role of a user instance we can just run user.role. Lazy parameter is how SQLAlchemy will load our projects. The lazy option is our objects will be loaded on access and filtered before returning.
    '''

    def __repr__(self):
        return f'User {self.name}'

class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review:

    all_reviews = []
    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):
        response = []
        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)
        return response
