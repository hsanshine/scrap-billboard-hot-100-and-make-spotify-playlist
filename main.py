# 2021-02-11
#program to scrap billboard hot 100 of top songs of a day you enter then make spotify playlist from the list
#by hamza

import requests
from bs4 import BeautifulSoup
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

# scope = 'user-read-recently-played'
scope = 'playlist-modify-private'
# scope = 'user-read-playback-state, user-modify-playback-state'

client_Id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

auth_manager = SpotifyOAuth(client_id = client_Id, client_secret=client_secret,scope=scope, show_dialog=True,
        cache_path="token.txt")
sp = spotipy.Spotify(auth_manager=auth_manager)

# #show playing devices
# res = sp.devices()
# pprint(res)
#
# #change track
# sp.start_playback(uris=['spotify:track:3GCdLUSnKSMJhs4Tj6CV3s'])
#
# #change volume
# for i in range(10):
#     sp.volume(100)
#
#     sleep(2)
#     sp.volume(50)
#
#     sleep(2)
#     sp.volume(20)

user_id = sp.current_user()["id"]
# print(user_id)
#

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billBoardUrl = f'https://www.billboard.com/charts/hot-100/{date}'

selectLocation = 'li span'
songClass = 'chart-element__information__song text--truncate color--primary'
artistNameClass = 'chart-element__information__artist text--truncate color--secondary'

response = requests.get(billBoardUrl)
soup = BeautifulSoup(response.text, "html.parser")

songs = [ song.getText() for song in soup.find_all('span', attrs={'class': songClass})]

artists = [artist.getText() for artist in soup.find_all('span', attrs={'class':artistNameClass})]



song_names = ["The list of song", "titles from your", "web scrape"]
song_names = songs;

song_uris = []
year = date.split("-")[0] # to get the year that was entered

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
        #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(result)
        print(f"{song} doesn't exist in Spotify. Skipped.")



#song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)





