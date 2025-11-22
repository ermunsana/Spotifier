import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("client"),
        client_secret=os.getenv("secret"),
        redirect_uri=os.getenv("redirect_uri"),
        scope="user-library-read"
    )
)

clairo_uri = 'spotify:artist:3l0CmX0FuQjFxr8SK7Vqag'

results = sp.artist_albums(clairo_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
