from sqlmodel import Relationship, Field, SQLModel, create_engine
from typing import List

###################
# This creates    #
# the databse and #
# the tables      #
###################


class TheBoys(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    full_name: str
    description: str
    image_url: str
    actor_name: str
    gender: str
    
    

class Episodes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ep_name: str
    season: str
    description: str



SQLITE_URL = "sqlite:///./database.db"

engine = create_engine(SQLITE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()