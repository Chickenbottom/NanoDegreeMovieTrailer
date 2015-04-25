Author: Chad Hickenbottom 
Nano Degree: Full Stack Web Developer
Project 1: Movie Trailer Website
Local Enviornments: Windows7 and Python3.4

ABOUT:
	This project will dynaimcally create a local webpage and launch on the users default browser. The webpage will contain all of the Star Wars movies(2015 and previous): Titles, posters and previews (embeded YouTube videos).

NOTES ABOUT PROGRAM:
	Changes Made to source code:
		Background color of page is hex value #333 which is the same as the text color; therefore, initially the title and description cannot be seen. The text color changes to white when the mouse hovers over the picture, making the title and description visable.

		Added .poster:hover{width:320;height:497;} to CSS contained in fresh_tomatoes.py. This increases the size of the poster when the mouse hovers over. 

		Changed the title and nav bar title to Star Wars! and Star Wars respectively.


WHAT TO RUN:
	To run program execute movies_page.py - requires python 2.7 or higher

HOW TO INSTALL PYTHON (Not required for Linux or iOS):
	This program requires python2.7 or better if you have not downloaded python you can download it at: https://www.python.org/downloads/
	Follow install prompts, take note of the path where python is installed.
	After installing you may add python to your local enviornment path variables, this will allow you to run python scripts from any directory on your computer. 
	To do this go to:
		Control Panel -> Advanced System Settings -> Enviornment Variables
		In User variables click "path" then the edit button.
		go to the "Variable Value" scroll to the end of the list add a semicolon(;) add the path to where you installed python the directory should contain "python.exe"

HOW TO RUN:	
	After installing there are a few ways in which to run the program:
		If you added python to the Environment Variables:
			double click movies_page.py
			open a command prompt window:
				windows key -> type in "cmd"
			change directory to movies_page.py
				"cd (type in your directory"
				hit enter
			type in "movies_page.py" 
			hit enter
		If you did NOT add python to Enviornement Variables:
			open a command prompt window:
				windows key -> type in "cmd"
			change directory to movies_page.py
				"cd (type in your directory"
				hit enter
			type in "python movies_page.py" 
			hit enter

