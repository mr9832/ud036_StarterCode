import webbrowser

class Movie():
    """
    ******************************************************************
    *  This class provides a way to store movie related information  *
    ******************************************************************
    """
    title                   = ""
    story_line              = ""
    poster_image_url        = ""
    trailer_youtube_url     = ""
    rating                  = ""

    #*****************************************************************
    #*  COnstructor: accepts and stored Movie details
    #*****************************************************************
    def __init__(self, title, storyLine, image, trailer, rating):
        VALID_RATINGS               = ["G", "PG", "PG-13", "R"]
        self.title                  = title
        self.story_line             = storyLine
        self.poster_image_url       = image
        self.trailer_youtube_url    = trailer
        self.rating                 = rating
        if rating not in VALID_RATINGS:
            self.rating = "Unknown"

#print(Movie.__doc__)

#**********************************************************************************
#*   Test
#**********************************************************************************
def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)

#mike = Movie("Toy Story", "A Story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.yutube.com/watch?v=vwyZH85NQC4", "PG")
#mike.show_trailer()

