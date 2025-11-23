
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
