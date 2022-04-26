class Review:

    all_reviews = []

    #Initialize a review and create an object
    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    #Save the object
    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    #Display reviews
    @classmethod
    def get_reviews(cls,id):
        response = []
        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)
        return response