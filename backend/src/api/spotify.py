import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()

scope = "user-library-read, user-read-email, user-read-private, user-follow-read, user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"),
                                               client_secret=os.getenv("CLIENT_SECRET"),
                                                redirect_uri=os.getenv("REDIRECT_URI"),
                                                scope=scope))


def user_saved_tracks(limit=10):
    results = sp.current_user_saved_tracks(limit=limit)
    tracks = []
    for item in results['items']:
        track = item['track']
        tracks.append({
            "artist": track['artists'][0]['name'],
            "name": track['name']
        })
    return tracks



def get_about_user():
    user = sp.current_user()
    return {
        "display_name": user['display_name'],
        "id": user['id'],
        "email": user['email'],
        "country": user['country'],
        "images": user['images']
    }



