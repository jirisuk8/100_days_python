import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

APP_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
APP_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=APP_CLIENT_ID,
                                                           client_secret=APP_CLIENT_SECRET))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])