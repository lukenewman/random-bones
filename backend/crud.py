from sqlalchemy.orm import Session
import random
import models

def get_episode(db: Session):
  rand = random.randrange(0, db.query(models.Episode).count()) 
  return db.query(models.Episode)[rand]

def get_episodes(db: Session):
  return db.query(models.Episode).all()