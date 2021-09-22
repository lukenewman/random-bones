from datetime import datetime
from pydantic import BaseModel

class EpisodeSchema(BaseModel):
  id: int
  name: str
  pub_date: datetime
  url: str

  class Config:
    orm_mode = True