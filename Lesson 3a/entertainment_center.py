import media
import fresh_tomatoes

#Creating Movie Objects
###movie_title, movie_storyline, poster_image, trailer_youtube
pirates_of_silicon_valley = media.Movie(movie_title = "Pirates of Silicon Valley",
				   poster_image = "http://upload.wikimedia.org/wikipedia/en/3/30/Movieposterposv.jpg",
				   trailer_youtube = "https://www.youtube.com/watch?v=lEyrivrjAuU",)
				   

queen_of_versailles = media.Movie("The Queen of Versailles", "http://foreveryoungadult.com/_uploads/images/29540/thequeenofversailles__span.jpg", "https://www.youtube.com/watch?v=AdJYzgJ4CwI")

jiro_dreams_of_sushi = media.Movie("Jiro Dreams of Sushi", "http://upload.wikimedia.org/wikipedia/en/4/47/Jiro_sushi_poster.jpg", "https://www.youtube.com/watch?v=I1UDS2kgqY8")

movies = [pirates_of_silicon_valley, queen_of_versailles, jiro_dreams_of_sushi]

fresh_tomatoes.open_movies_page(movies)
