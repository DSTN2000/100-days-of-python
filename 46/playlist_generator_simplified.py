import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from chart_scraper import *

CLIENT_ID = '3fb223cf753a435a9ad610537ec7da45'
CLIENT_SECRET = 'c68ec3fe0c074e4c808b113374b6ebba'
USER_ID = '31fmgt2bjfcf7hrb2rh7glgsihw4'

#scope = "user-library-read"
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://example.com', scope=scope))

date = input('Type the date in this format: YYYY-MM-DD: \n')
songs = get_chart_data(date)

#print(sp.current_user())
playlist = sp.user_playlist_create(USER_ID, f'{date} Billboard Hot 100', public=False)
playlist_id = playlist['id']

playlist_songs = []
for song in songs:
    title, artist = song
    artist = artist.replace('Featuring', '').replace('&', '')
    #print(title, artist)
    results = sp.search(q=f'{title} artist:{artist}', type='track')
    items = results['tracks']['items']
    try:
        new_song_uri = items[0]['uri']
        playlist_songs.append(new_song_uri)
    except:
        artist = ' '.join(artist.split())
        print(title, artist)
        results = sp.search(q=f'{title} {artist.split()[0]}', type='track', limit=50)
        items = results['tracks']['items']
        try:
            for item in items:
                #pprint(item)
                found_match = False
                new_song_artists = [artist['name'].lower() for artist in item['artists']]
                print(new_song_artists)
                for new_artist in new_song_artists:
                    if new_artist in artist.lower(): 
                        print(new_artist, artist.lower())
                        new_song_uri = item['uri']
                        found_match = True
                        break
                if found_match:
                    break
            playlist_songs.append(new_song_uri)
            print('success')
        except:
            print('test')
        

sp.user_playlist_add_tracks(USER_ID, playlist_id=playlist_id, tracks=playlist_songs)


