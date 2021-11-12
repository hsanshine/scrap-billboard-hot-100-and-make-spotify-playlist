# 2021-02-11
#program to scrap billboard hot 100 of top songs of a day you enter then make sportify playlist from the list
#by hamza

import requests
from bs4 import BeautifulSoup
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_Id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

print(client_Id)

# userDate= input('enter the date of songs in yyyy-mm-dd format : ')
# date = userDate
# billBoardUrl = f'https://www.billboard.com/charts/hot-100/{date}'
#
# selectLocation = 'li span'
# songClass = 'chart-element__information__song text--truncate color--primary'
# artistNameClass = 'chart-element__information__artist text--truncate color--secondary'
# print(billBoardUrl)
# response = requests.get(billBoardUrl)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title)
# songs = [ song.getText() for song in soup.find_all('span', attrs={'class': songClass})]
# print(len(songs))
# print(songs)
# artists = [artist.getText() for artist in soup.find_all('span', attrs={'class':artistNameClass})]
# print(len(artists))
# print(artists)





