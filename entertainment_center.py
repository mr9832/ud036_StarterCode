import Movie_Media    as media
import fresh_tomatoes as fresh_tomatoes

movies = []
#********************************************************************************
#*  Here we load all the Movies from a file named <movie_configurations.txt>
#********************************************************************************
try:
    FileIn = open('movie_configurations.txt')
    print(" ")
    print("Loaded these Movies ")
    print("=================== ")
    lineIn = FileIn.readline()
    while lineIn:
        if lineIn[0] == '#':
            next
        split = lineIn.split('|')
        if (split.__len__() == 5):
            aMovie = media.Movie(split[0], split[1], split[2], split[3], split[4])
            print(aMovie.title)
            movies.append(aMovie)
        lineIn = FileIn.readline()
    FileIn.close()

except Exception as err:
    print("")
    print("**********************************************************************")
    print("*  Exception:", err, "*")
    print("**********************************************************************")
    print("")

#********************************************************************************
#*  Here we present a web page with all the movies from the movie config file
#********************************************************************************
fresh_tomatoes.open_movies_page(movies)

#********************************************************************************
#*  Here we present a web page with a single requested (by Title) movie
#********************************************************************************
def play_a_single(platThis):
    for movie in movies:
        this_title = str(movie.title)
        if this_title.lower() == platThis.lower():
            single = []
            single.append(movie)
            fresh_tomatoes.open_movies_page(single)
#********************************************************************************
#play_a_single("Small Fry")

