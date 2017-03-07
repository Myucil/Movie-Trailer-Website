

# Parent class
class Video():
    def __init__(self, movie_title, movie_duration):
        self.title = movie_title
        self.duration = movie_duration


# Child class of video
class Movie(Video):
    def __init__(self, movie_title, movie_duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
