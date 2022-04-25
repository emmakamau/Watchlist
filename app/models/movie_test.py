import unittest
from models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
        print(self.new_movie)

    def test_instance(self):
        '''
        We then define a test case test_instance that uses the isinstance() function that checks if the object self.new_movie is an instance of the Movie class.
        '''
        self.assertTrue(isinstance(self.new_movie,Movie))


if __name__ == '__main__':
    unittest.main()