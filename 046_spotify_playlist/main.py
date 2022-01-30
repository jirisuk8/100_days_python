# import spotipy
import os
from billboard_webscrape import get_songs_from_billboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = "https://example.com"

# Create a Spotify API Client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private"
    )
)
# Get current user details
user_id = sp.current_user()["id"]

# Select date and get list of songs
songs, date = get_songs_from_billboard()
song_uris = []
for song in songs:
    result = sp.search(q=f"track:{song} year:{date.split('-')[0]}", type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} could not be find in Spotify and has been skipped.")

# Create a Spotify Playlist and get the Playlist ID
playlist_name = f"{date} Billboard hot 100"
response = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    collaborative=False,
    description='Hot 100 from billboard.com'
)
playlist_id = response["id"]

# add items to playlist
response_playlist_filled = sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris
)
print(f"Enjoy your playlist here: {response['external_urls']['spotify']}")
