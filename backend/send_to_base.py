import models, crud
from deta import Deta

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./episodes.db"

engine = create_engine(
  SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

deta = Deta("b0y2ugtg_97RSrN6cYpBN4DCK9n5Np85wKYZz4Rxh")

episodes = deta.Base("episodes")

for index, episode in enumerate(crud.get_episodes(db=db), start=1):
  episodes.insert({
    "index": index,
    "name": episode.name,
    "url": episode.url
  })

db.close()
