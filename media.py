import webbrowser


# create a class called Movie and this is used in entertainment_center.py
class Movie:
    Valid_Ratings = ["G", "PG", "PG-13", "R"]

    # init the class, Movie, by intaking 4 inputs excluding self.
    def __init__(self, movie_title, movie_info, poster_image, trailer_youtube):
        # define class variables using inputs
        self.title = movie_title
        self.movieInfo = movie_info
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # open the youtube video.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
