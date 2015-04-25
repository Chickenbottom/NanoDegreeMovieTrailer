#   Author: Chad Hickenbottom 
#   Nano Degree: Full Stack Web Developer
#	media.py:   Version: 1.0

#    this program creates movie objects


import webbrowser


class Movie():
	def __init__(self, title, desc, poster, trailer):
		self.title = title
		self.storyline = desc
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer

#   open default webbrowser to youtube url
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
#   open default webbrowser to poster url
	def show_poster(self):
		webbrowser.open(self.poster_image_url)
