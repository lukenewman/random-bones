from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Episode(Base):
  __tablename__ = "episode"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(200))
  pub_date = Column(DateTime)
  url = Column(String(200))