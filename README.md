# Movie-Library
A python application that finds the imdb score and director(s) of movies.

This Desktop app is made with Python 3.8, and uses imdbPy and PyQt5 for the GUI components.

The repo contains several files :
  - gui.py : use this file to launch the interface of the app.
  - project.py : contains the logic of the app ( connecting to the imdbPy API and looking through the text files )
  - ids.txt : contains the imdb ids of movies that are used to look for each movie in the API.
  - mvs.txt : contains a sample of the movies that can be given to the app in the format  movie_name (year) resolution.
  - mvs short.txt : similar to mvs (was used during testing).

Workings of the App:
  - launch the app by running gui.py.
  - click on load file button.
  - navigate to the location and select the .txt file containing the movies information in the format stated before.
  - After clicking on open, wait for a few seconds (this will depend on the length of the list and the computer, as well as the response time of the API)
  - The app will display the movies given and their imdb scores and the name of the director.
  - You can save the results to your desktop by clicking on save results. 

Limitations:
  - the app is limited by the response time of the API, if a huge list is given the result might take some time to be shown.
  - giving an invalid name/date will make the app skip the movie completely.
  
Proposed improvements and modification for the future :
  - implement the interface using Tkinter or switch to a web interface.
  - Use regex.
  - Swithch to another faster API or use web scraping.
  - Implement a progress bar.
