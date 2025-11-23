import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"),
                                               client_secret=os.getenv("CLIENT_SECRET"),
                                                redirect_uri=os.getenv("REDIRECT_URI"),
                                                scope=scope))


def get_most_played(limit=10):
    results = sp.current_user_saved_tracks(limit=limit)
    tracks = []
    for item in results['items']:
        track = item['track']
        tracks.append({
            "artist": track['artists'][0]['name'],
            "name": track['name']
        })
    return tracks