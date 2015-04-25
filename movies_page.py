#   Author: Chad Hickenbottom 
#   Nano Degree: Full Stack Web Developer
#   movies_page: Version: 1.0
#   dependencies: python2.7 or greater, media.py, fresh_tomatoes.py

#   This program generates a list of movie objects and calls fresh_tomatoes.py which dynamically creates a local webpage.


import media
import fresh_tomatoes

the_phantom_menace = media.Movie("Star Wars:<br>The Phantom Menace", "Midichlorians are the Force.", 
						"http://upload.wikimedia.org/wikipedia/en/thumb/4/40/Star_Wars_Phantom_Menace_poster.jpg/220px-Star_Wars_Phantom_Menace_poster.jpg",
						"https://www.youtube.com/watch?v=bD7bpG-zDJQ")

attack_of_the_clones = media.Movie("Star Wars:<br>Attack of the Clones", "Worst love story... ever", 
						"http://img1.wikia.nocookie.net/__cb20130822173923/starwars/images/2/24/EPII_AotC_poster.png", 
						"https://www.youtube.com/watch?v=CO2OLQ2kiq8")

revenge_of_the_sith = media.Movie("Star Wars:<br>Revenge of the Sith", "A villian is born", 
					"http://ia.media-imdb.com/images/M/MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@._V1_SX640_SY720_.jpg",
					"https://www.youtube.com/watch?v=a3Cdj3GpobM")

a_new_hope = media.Movie("Star Wars:<br>A New Hope", "Han shoots first, no really...", 
						"http://cdn.collider.com/wp-content/uploads/star-wars-movie-poster.jpg", 
						"https://www.youtube.com/watch?v=vZ734NWnAHA")

empire_strikes_back = media.Movie("Star Wars:<br>Empire Strikes Back", "The bad guy is related to the Good guy!", 
						"https://www.movieposter.com/posters/archive/main/4/A70-2036", 
						"https://www.youtube.com/watch?v=96v4XraJEPI")

return_of_the_jedi = media.Movie("Star Wars:<br>The Return of the Jedi", "Hayden Christensen was 2 years old and not a ghost",
						"http://img1.wikia.nocookie.net/__cb20050925102019/starwars/images/4/44/Return_of_the_jedi_old.jpg",
						"https://www.youtube.com/watch?v=7L8p7_SLzvU")

the_force_awakens = media.Movie("Star Wars:<br>The Force Awakens", "CAN'T WAIT!!!",
						"http://mytimelesscool.net/wp-content/uploads/2014/11/the-force-awakens.jpg",
						"https://www.youtube.com/watch?v=wCc2v7izk8w")



movie_list = [the_phantom_menace, attack_of_the_clones, revenge_of_the_sith, a_new_hope, empire_strikes_back, return_of_the_jedi, the_force_awakens]

#####Uncomment the for-loop to test all movies trailer and movie poster URLS 
#####The functions do not test if the url are valid but rather will open browsers with the urls 
#####You must check each tab or window that opens for correct content.
# for movie in movie_list:  
# 	movie.show_trailer()
# 	movie.show_poster()


# send list to fresh_tomatoes.py 
# that function dynamically creates a local webpage and automatically opens it in the default browser
fresh_tomatoes.open_movies_page(movie_list)

