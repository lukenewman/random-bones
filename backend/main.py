from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from deta import Deta
import random

app = FastAPI()

origins = [
  "http://localhost:3001",
  "https://614bad3ea307184417a60adb--random-bones.netlify.app/"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

deta = Deta("b0y2ugtg_97RSrN6cYpBN4DCK9n5Np85wKYZz4Rxh")
episodes = deta.Base("episodes")

@app.get("/episode")
def get_episode():
  index = random.randrange(1, 1982)
  return episodes.fetch({"index": index})