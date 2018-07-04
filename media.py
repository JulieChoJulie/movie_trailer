import webbrowser


# create a class called Movie and this is used in entertainment_center.py
class Movie:
    Valid_Ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_info, poster_image, trailer_youtube):
        self.title = movie_title
        self.movieInfo = movie_info
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        """

        Args:
            movie_title (str): the title of the movie in string form
            movie_info (str): it is in html format using <p> tags.
            poster_image (str): it represents url of the poster of the movie.
            trailer_youtube (str): it represents url of the youtube trailer.

        """

    # open the youtube video.
    @property
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        """

        Args:
            self : self has four different attr defined by __init__.
        returns:
            it returns youtube trailer opens using default web browser by
            taking self.trailer_youtube_url, which is the fourth arguments
            when the class is initiated.

        """
