import requests
import json
import math
import random

#client information found in Spotify API
clientID = ""
clientSecret = ""
#Make sure to update this as it expires often
clientToken = ""

#The account to be accessed
userID = "bigb_035"
playlistID = ""

# Validate this is up to date make sure to round up to the nearest 20 divisible
current_count = 1240
all_songs = []

library_headers = {
    "Content-Type":"application/json",
    "Authorization":"Bearer {}".format(clientToken)
}

def createPlaylist():
    global playlistID
    
    request_body = json.dumps({
        "name": "Favs Sep 2020 TEST",
        "description": "Fav 64 songs at the moment as of 09/01/2020 UNDER CONSTRUCTION",
        "public": True
    })
    query = "https://api.spotify.com/v1/users/"+userID+"/playlists"
    response = requests.post(
        query,
        data=request_body,
        headers={
            "Content-Type":"application/json",
            "Authorization": "Bearer "+clientToken
        }
    )
    response_json = json.loads(response.text)
    playlistID = response_json["id"]
    print(response_json["id"])
    
def checkLibrary():
    global current_count
    query = "https://api.spotify.com/v1/me/tracks"
    
    response = requests.get(query,headers=library_headers)
    response_json = json.loads(response.text)
    count_songs = response_json["total"]
    #print(count_songs)
    
    if count_songs > current_count:
        current_count = count_songs

def loadSongs():
    global current_count
    global all_songs

    all_songs_raw = []

    for i in range (int(math.ceil(current_count/20.0))):
        offset = 20*i
        url = "https://api.spotify.com/v1/me/tracks?limit20&offset={}".format(offset)
        response = requests.get(url, headers=library_headers)
        parsed = json.loads(response.text)
        #print(len(parsed["items"]))
        all_songs_raw.extend(parsed["items"])

    for song in all_songs_raw:
        track_id = song["track"]["uri"]
        all_songs.append(track_id)

    random.shuffle(all_songs)
    random.shuffle(all_songs)
    #print(len(all_songs))

def addToPlaylist():
    query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlistID)
    temp_list = []
    for i in all_songs:
        temp_list.append(i)
        if(len(temp_list) >= 20):
            print(len(temp_list))
            request_data = json.dumps({"uris":temp_list})
            print(temp_list)
            response = requests.post(
                query,
                data = request_data,
                headers = library_headers
            )
            temp_list = []
    if(len(temp_list) % 20 != 0):
        print(len(temp_list))
        request_data = json.dumps({"uris":temp_list})
        print(temp_list)
        response = requests.post(
            query,
            data = request_data,
            headers = library_headers
        )
        temp_list = []
    
if __name__ == "__main__":
    #createPlaylist()
    checkLibrary()
    print(current_count)
    #loadSongs()
    #addToPlaylist()
