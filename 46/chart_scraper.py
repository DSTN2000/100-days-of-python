import requests as r, pandas as pd
from bs4 import BeautifulSoup as bs

def get_chart_data(date):
    URL = f'https://www.billboard.com/charts/hot-100/{date}'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

    print(URL)

    responce = r.get(URL, headers=headers)
    soup = bs(responce.text, 'html.parser')
    songs = soup.select('li ul li h3') #returns the elements containing the title of a song (locating artist name with css is harder due to Billboard's html structure)
    #title and artist name are inside of the same li element
    songs = [(song_title.string.strip(), song_artist.string.strip()) for (song_title, song_artist) in [song_title.parent.findChildren() for song_title in songs]]
    return songs