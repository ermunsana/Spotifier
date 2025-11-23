from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware

from .api.spotify import get_most_played

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/most-played")
def most_played():
      return get_most_played()
