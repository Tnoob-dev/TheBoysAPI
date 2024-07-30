from sqlmodel import Field, SQLModel, create_engine

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

SQLITE_URL = "sqlite:///./database.bd"

engine = create_engine(SQLITE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
if __name__ == "__main__":
    create_db_and_tables()