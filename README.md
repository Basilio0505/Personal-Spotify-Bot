# Personal-Spotify-Bot

The spotify_makePlaylist.py file is my personal Spotify program that can run 4 different 
methods utilizing Spotify API calls. I use this program to help create my quarterly Spotify 
playlist as it automatically randomizes all my songs in my library and puts it into one playlist
for me to sort through.

createPlaylist() will create a new playlist with name, desc, and public status set.

checkLibrary() will check the user music library and return the total amount of songs saved.

loadSongs() will read all the songs in the user music library and places them into a list
after being randomized.

addToPlaylist() will add the list of randomized songs into the newly created playlist in groups 
of 20 since Spotify API only allows up to 20 songs per query.