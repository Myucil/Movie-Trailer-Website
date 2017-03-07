import fresh_tomatoes
import media
import urllib
import ast

# API that takes in the imdb ID of a movie and returns it's info
def movie_id(id):
    api = urllib.urlopen("http://www.omdbapi.com/?i=" + id + "&plot=short&r=json")
    read_info = api.read()
    movie_json = ast.literal_eval(read_info)
    return movie_json


# Calls movie_id and returns the necessary movie info

movie_info = movie_id("tt0145487")
spiderman = media.Movie(movie_info.get("Title"),
                        movie_info.get("Runtime"),
                        movie_info.get("Plot"),
                        movie_info.get("Poster"),
                        "http://www.youtube.com/watch?v=O7zvehDxttM")

movie_info = movie_id("tt2488496")
starwars = media.Movie(movie_info.get("Title"),
                       movie_info.get("Runtime"),
                       movie_info.get("Plot"),
                       movie_info.get("Poster"),
                       "http://www.youtube.com/watch?v=sGbxmsDFVnE")

movie_info = movie_id("tt0381061")
casino_royale = media.Movie(movie_info.get("Title"),
                            movie_info.get("Runtime"),
                            movie_info.get("Plot"),
                            movie_info.get("Poster"),
                            "http://www.youtube.com/watch?v=36mnx8dBbGE")

movie_info = movie_id("tt2294629")
frozen = media.Movie(movie_info.get("Title"),
                     movie_info.get("Runtime"),
                     movie_info.get("Plot"),
                     movie_info.get("Poster"),
                     "http://www.youtube.com/watch?v=TbQm5doF_Uc")

movie_info = movie_id("tt3659388")
the_martian = media.Movie(movie_info.get("Title"),
                          movie_info.get("Runtime"),
                          movie_info.get("Plot"),
                          movie_info.get("Poster"),
                          "http://www.youtube.com/watch?v=ej3ioOneTy8")

movie_info = movie_id("tt2911666")
john_wick = media.Movie(movie_info.get("Title"),
                        movie_info.get("Runtime"),
                        movie_info.get("Plot"),
                        movie_info.get("Poster"),
                        "http://www.youtube.com/watch?v=2AUmvWm5ZDQ")


#Made an array of the movies and called fresh_tomates.open_movies_page to create the movie trailer website
movies = [spiderman, starwars, casino_royale, frozen, the_martian, john_wick]
fresh_tomatoes.open_movies_page(movies)