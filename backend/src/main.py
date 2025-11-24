from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.spotify import user_saved_tracks
from .api.spotify import get_about_user
from .api.spotify import get_following_artists

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Spotifier API"}

@app.get("/saved-tracks")
def saved_tracks():
      return user_saved_tracks()


@app.get("/about-user")
def about_user_route():
    return get_about_user()

@app.get("/following-artists")
def following_artists_route():
    return get_following_artists()